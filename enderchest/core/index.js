import { glob } from 'glob';
import { EnderChest } from "./EnderChest.js";
import { Logger } from "./utils/Logger.js";
import { Settings } from "./utils/Settings.js";
import { EnderChestContent } from './EnderChestContent.js';

function initialize() {
  if (!Settings.secretKey) {
    Logger.error('SOURCE CODE NOT ENCRYPTED >> The "secretKey" settings was not parsed in filter configuration.');
    return;
  }

  if (!Settings.isValidKeyBitsSize()) {
    Logger.error(`SOURCE CODE NOT ENCRYPTED >> The "keySize" value of ${Settings.keySize} is not valid. The options are 128, 192 or 256.`);
    return;
  }

  if (!Settings.isValidSecretKey()) {
    Logger.error(`SOURCE CODE NOT ENCRYPTED >> The length of "secretKey" should be ${Settings.keySize / 8} for ${Settings.keySize}-bits. The parsed length was ${Settings.secretKey.length}.`);
    return;
  }

  const cryptedText = EnderChest.encrypt('namespace:identifier');

  glob(["BP/**/*.json"]).then((file) => {
    EnderChest.identifier.encryptAndSave(file[2]);

    console.log(JSON.stringify(EnderChestContent.CONTENT.get('ae82-ab4c')));
  });

}

initialize();