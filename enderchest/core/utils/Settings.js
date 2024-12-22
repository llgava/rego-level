const args = process.argv[2] ? JSON.parse(process.argv[2]) : {};

export class Settings {
  static keySize = args.keySize || 192;
  static secretKey = args.secretKey || undefined;
  static ignore = args.ignore || [];

  static isValidKeyBitsSize() {
    return this.keySize === 64  ||
           this.keySize === 128 ||
           this.keySize === 192 ||
           this.keySize === 256;
  }

  static isValidSecretKey() {
    if (!this.secretKey) return false;

    return (this.secretKey.length * 8) === this.keySize;
  }
}