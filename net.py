import speedtest

def measure_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    ping = st.results.ping  # Ping in ms
    
    return download_speed, upload_speed, ping

if __name__ == "__main__":
    download_speed, upload_speed, ping = measure_speed()
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed: {upload_speed:.2f} Mbps")
    print(f"Ping: {ping} ms")

print("---")





# import speedtest
# import time

# def measure_speed():
#     st = speedtest.Speedtest()
#     st.get_best_server()
    
#     start_time = time.time()
#     download_speed = st.download() / 1_000_000  # Convert to Mbps
#     end_time = time.time()
#     download_time = end_time - start_time
    
#     start_time = time.time()
#     upload_speed = st.upload() / 1_000_000  # Convert to Mbps
#     end_time = time.time()
#     upload_time = end_time - start_time
    
#     ping = st.results.ping  # Ping in ms
    
#     return download_speed, upload_speed, ping, download_time, upload_time

# if __name__ == "__main__":
#     download_speed, upload_speed, ping, download_time, upload_time = measure_speed()
#     print(f"Download Speed: {download_speed:.2f} Mbps (Time: {download_time:.2f} seconds)")
#     print(f"Upload Speed: {upload_speed:.2f} Mbps (Time: {upload_time:.2f} seconds)")
#     print(f"Ping: {ping} ms")



# print("---")








