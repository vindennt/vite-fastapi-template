# import time
# import logging
# from fastapi import Request

# logging.getLogger("uvicorn.access").disabled = True
# logger = logging.getLogger("uvicorn")

# # Middleware to log request and response details
# # This middleware logs the request method, path, protocol, client IP and port,
# # and the response status code, content length, and processing time.
# # TODO: Make more robust
# # Reimplement with # app.middleware("http")(mw_logger) in main.py
# async def mw_logger(request: Request, call_next):
#     start_time = time.perf_counter()

#     protocol = request.url.scheme
#     client_ip = request.client.host
#     client_port = request.client.port

#     logger.info(
#         f"> r | Method: {request.method} | Path: {request.url.path} | Protocol: {protocol.upper()} | IP: {client_ip}:{client_port}"
#     )
    
#     # Handle request and measure duration
#     response = await call_next(request)
#     process_time = (time.perf_counter() - start_time) * 1000

#     content_length = response.headers.get("content-length")
#     content_length = int(content_length) if content_length else 0
    
#     logger.info(
#         f"< s | Method: {request.method} | Path: {request.url.path} | Status: {response.status_code} | IP: {client_ip}:{client_port} | Duration: {process_time:.2f}ms"
#     )

#     return response
