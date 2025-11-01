"""
API client for Website Launches API
"""
import requests


class WeblAPIClient:
    """Client for interacting with Website Launches Domain Intelligence API"""

    def __init__(self, api_key=None, base_url="https://websitelaunches.com/api/v1"):
        self.api_key = api_key
        self.base_url = base_url
        self.session = requests.Session()

        # Set User-Agent
        self.session.headers.update({
            'User-Agent': 'webl-cli/0.1.0'
        })

        # Only add API key header if provided
        if api_key:
            self.session.headers.update({
                'X-API-Key': api_key
            })

    def lookup_domain(self, domain, history=False):
        """
        Lookup domain intelligence

        Args:
            domain: Domain name to lookup (e.g., 'github.com')
            history: Include historical authority data (default: False)

        Returns:
            dict: API response data
        """
        url = f"{self.base_url}/domain/{domain}"
        params = {}

        if history:
            params['history'] = 'true'

        try:
            response = self.session.get(url, params=params, timeout=30)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise APIError("Invalid API key. Remove your API key config or set a valid one.")
            elif e.response.status_code == 429:
                # Try to parse error response for better message
                try:
                    error_data = e.response.json()
                    if error_data.get('error', {}).get('tier') == 'anonymous':
                        used = error_data['error'].get('used', 0)
                        limit = error_data['error'].get('limit', 3000)
                        resets = error_data['error'].get('resets_at', 'next month')
                        raise APIError(f"Free tier limit exceeded ({used}/{limit} requests). Sign up for an API key at https://websitelaunches.com/api/ or wait until {resets}")
                except:
                    pass
                raise APIError("Rate limit exceeded. Upgrade your plan at https://websitelaunches.com/api/ or wait before retrying.")
            elif e.response.status_code == 404:
                raise APIError(f"Domain '{domain}' not found in our database.")
            else:
                raise APIError(f"API error: {e.response.status_code} - {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")

    def batch_lookup(self, domains, history=False):
        """
        Batch lookup multiple domains

        Args:
            domains: List of domain names
            history: Include historical authority data (default: False)

        Returns:
            dict: API response data
        """
        url = f"{self.base_url}/domain/batch"
        payload = {
            'domains': domains
        }

        if history:
            payload['history'] = True

        try:
            response = self.session.post(url, json=payload, timeout=60)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 401:
                raise APIError("Invalid API key. Run 'webl config set-key YOUR_KEY' to set your API key.")
            elif e.response.status_code == 429:
                raise APIError("Rate limit exceeded. Please upgrade your plan or wait before retrying.")
            else:
                raise APIError(f"API error: {e.response.status_code} - {e.response.text}")
        except requests.exceptions.RequestException as e:
            raise APIError(f"Network error: {str(e)}")


class APIError(Exception):
    """Exception raised for API errors"""
    pass
