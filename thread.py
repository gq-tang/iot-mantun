import threading

class ReadWriteLock:
    def __init__(self):
        self.read_lock = threading.Lock()
        self.write_lock = threading.Lock()
        self.reader_count = 0

    def acquire_read(self):
        """获取读锁"""
        with self.read_lock:
            self.reader_count += 1
            if self.reader_count == 1:
                self.write_lock.acquire()  # 第一个读线程获取写锁

    def release_read(self):
        """释放读锁"""
        with self.read_lock:
            self.reader_count -= 1
            if self.reader_count == 0:
                self.write_lock.release()  # 最后一个读线程释放写锁

    def acquire_write(self):
        """获取写锁"""
        self.write_lock.acquire()

    def release_write(self):
        """释放写锁"""
        self.write_lock.release()
