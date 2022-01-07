import logging
import os
import time


class Logger:
    __slots__ = ["_logger", "_stream_handler", "_formatter", "_file_handler"]

    def __init__(self, name, log_save_path="./log", log_save_name=f"{time.strftime('%Y%m%d', time.localtime(time.time()))}.log",
                 level=logging.INFO):
        self._logger = logging.getLogger(name)
        self._logger.setLevel(level)
        self._stream_handler = logging.StreamHandler()
        if not os.path.exists(log_save_path):
            os.mkdir(log_save_path)
        log_save_path = f"{log_save_path}/{log_save_name}"
        self._file_handler = logging.FileHandler(filename=log_save_path, encoding="utf-8")

        self._formatter = logging.Formatter(
            "%(asctime)s %(name)s %(levelname)s %(filename)s-Process:%(process)d-Thread:%(thread)d-%(funcName)s-%(lineno)d: %(message)s")
        self._stream_handler.setFormatter(self._formatter)
        self._file_handler.setFormatter(self._formatter)
        self._logger.addHandler(self._stream_handler)
        self._logger.addHandler(self._file_handler)

    @property
    def logger(self):
        return self._logger

    @property
    def d(self):
        return self._logger.debug

    @property
    def i(self):
        return self._logger.info

    @property
    def w(self):
        return self._logger.warning

    @property
    def e(self):
        return self._logger.error

if __name__ == '__main__':
    log = Logger(__name__)
    log.d("12313")
    log.i({"12313"})
    log.w(["12313"])
    log.e(("12313",))


