import requests
from typing import Dict, Any, Optional

class HttpClient:
    def __init__(self, base_url: str = ""):
        """
        :param base_url: 可选的基础URL，例如 https://api.xxx.com
        """
        self.base_url = base_url.rstrip("/")

    def _build_url(self, url: str) -> str:
        if url.startswith("http"):
            return url
        return f"{self.base_url}{url.lstrip("/")}"

    # =========================
    # GET 请求
    # =========================
    def get(
        self,
        url: str,
        params: Optional[Dict[str, Any]] = None,
        headers: Optional[Dict[str, str]] = None,
        timeout: int = 10,
    ):
        full_url = self._build_url(url)

        try:
            response = requests.get(
                full_url,
                params=params,
                headers=headers,
                timeout=timeout,
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # POST 请求
    # =========================
    def post(self,
             url: str,
             data: Optional[Dict[str, Any]] = None,
             json_data: Optional[Dict[str, Any]] = None,
             headers: Optional[Dict[str, str]] = None,
             timeout: int = 10):
        full_url = self._build_url(url)

        try:
            response = requests.post(
                full_url,
                data=data,
                json=json_data,
                headers=headers,
                timeout=timeout,
            )

            return self._handle_response(response)

        except requests.RequestException as e:
            return {
                "success": False,
                "error": str(e)
            }

    # =========================
    # 统一响应处理
    # =========================
    @staticmethod
    def _handle_response(response: requests.Response):
        try:
            data = response.json()
        except ValueError:
            data = response.text

        return {
            "success": response.ok,
            "status_code": response.status_code,
            "data": data,
            "headers": dict(response.headers),
        }
