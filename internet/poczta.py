import smtplib

def main():
    from_addr = "konrad@example.com"
    to_addrs = ["konrad@example.com"]
    msg = "Hello World"
    with smtplib.SMTP("52.50.100.255", 5025) as server:
        msg = f"From: {from_addr}\nTo: {', '.join(to_addrs)}\n\n{msg}"
        server.sendmail(from_addr, to_addrs, msg)


if __name__ == "__main__":
    main()
