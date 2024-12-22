export class Logger {
  static info(message) {
    console.log(`\x1b[32mi ${message}\x1b[0m`)
  }

  static success(message) {
    console.log(`\x1b[32m✔ ${message}\x1b[0m`);
  }

  static warn(message) {
    console.log(`\x1b[33m! ${message}\x1b[0m`);
  }

  static error(message) {
    console.log(`\x1b[31mx ${message}\x1b[0m`);
  }
}