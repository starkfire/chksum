import hashlib
import fire

class Chksum:

    def sha1(self, filename):
        sha1 = hashlib.sha1()
        self._verify(filename, sha1)
    
    def sha256(self, filename):
        sha256 = hashlib.sha256()
        self._verify(filename, sha256)
    
    def sha384(self, filename):
        sha384 = hashlib.sha384()
        self._verify(filename, sha384)
    
    def sha512(self, filename):
        sha512 = hashlib.sha512()
        self._verify(filename, sha512)
    
    def _verify(self, file, hashFunction):
        with open(file, 'rb') as f:
            for byte_block in iter(lambda: f.read(4096), b''):
                hashFunction.update(byte_block)
            print(hashFunction.hexdigest())
    
    def help(self):
        return """
        Syntax: python chksum.py [sha1 | sha256 | sha384 | sha512] <filename>

        Example:
            python chksum.py sha256 'readme.txt'
        """

if __name__ == "__main__":
    fire.Fire(Chksum)