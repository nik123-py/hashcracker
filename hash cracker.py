import hashlib
import time


class HashCracker:
    def __init__(self, hash_to_crack, hash_type, wordlist):
        self.hash_to_crack = hash_to_crack
        self.hash_type = hash_type.lower()
        self.wordlist = wordlist

    def hash_word(self, word):
        """
        Hashes a word using the specified hash type.

        :param word: The word to hash.
        :return: The hashed value of the word.
        """
        word = word.strip()
        try:
            if self.hash_type == "md5":
                return hashlib.md5(word.encode()).hexdigest()
            elif self.hash_type == "sha1":
                return hashlib.sha1(word.encode()).hexdigest()
            elif self.hash_type == "sha256":
                return hashlib.sha256(word.encode()).hexdigest()
            else:
                raise ValueError(f"Unsupported hash type: {self.hash_type}")
        except Exception as e:
            print(f"Error hashing word: {word}, Error: {e}")
            return None

    def crack_hash(self):
        """
        Attempts to crack the hash using the wordlist.

        :return: The cracked password or None if not found.
        """
        print(f"[INFO] Starting hash cracking for {self.hash_to_crack} using {self.hash_type}...")
        start_time = time.time()
        for idx, word in enumerate(self.wordlist, 1):
            hashed_word = self.hash_word(word)
            if hashed_word == self.hash_to_crack:
                elapsed_time = time.time() - start_time
                print(f"[SUCCESS] Password found: '{word}' in {elapsed_time:.2f} seconds after {idx} attempts.")
                return word
            if idx % 100 == 0:
                print(f"[INFO] {idx} attempts made so far...")

        print("[FAILURE] Password not found in the wordlist.")
        return None

    @staticmethod
    def load_wordlist(file_path):
        """
        Loads a wordlist from a file.

        :param file_path: Path to the wordlist file.
        :return: A list of words from the file.
        """
        try:
            with open(file_path, "r") as file:
                print(f"[INFO] Loaded wordlist from {file_path}")
                return file.readlines()
        except FileNotFoundError:
            print(f"[ERROR] Wordlist file not found: {file_path}")
            return []
        except Exception as e:
            print(f"[ERROR] Failed to load wordlist: {e}")
            return []


# Example usage
if __name__ == "__main__":
    # Input hash to crack and hash type
    hash_to_crack = input("Enter the hash to crack: ").strip()
    hash_type = input("Enter the hash type (md5, sha1, sha256): ").strip()

    # Load wordlist
    wordlist_file = input("Enter the path to the wordlist file (or press Enter to use default): ").strip()
    if wordlist_file:
        wordlist = HashCracker.load_wordlist(wordlist_file)
    else:
        wordlist = [
            "password", "123456", "123456789", "qwerty", "abc123", "monkey", "12345678", "letmein",
            "111111", "123123", "iloveyou", "password1", "sunshine", "1234567", "princess", "admin",
            "welcome", "666666", "football", "password123"
        ]

    if not wordlist:
        print("[ERROR] No words loaded in the wordlist. Exiting.")
    else:
        cracker = HashCracker(hash_to_crack, hash_type, wordlist)
        cracker.crack_hash()
