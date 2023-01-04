from socketserver import TCPServer, StreamRequestHandler


class PulseHandler(StreamRequestHandler):
    def handle(self) -> None:
        pulse_data = self.rfile.readline()
        print(pulse_data)
        self.wfile.write(pulse_data + b'\n')
        confirm = self.rfile.readline()
        if confirm == 1:
            print(pulse_data, 'success')
        else:
            print(pulse_data, 'failed')


def main():
    with TCPServer(('localhost', 10001), PulseHandler) as pulse_tcp_server:
        # shut down with <CTRL-C>
        pulse_tcp_server.serve_forever()


if __name__ == 'main':
    main()
