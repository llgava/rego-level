import fs from 'fs';
import path from 'path';
import Handlebars from 'handlebars';
import { Logger } from "../utils/Logger.js";
import { EnderChestContent } from "../EnderChestContent.js";
import { fileURLToPath } from 'url';
import { Settings } from '../utils/Settings.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

export class VerySimpleScriptWrintingTextFile {

  static buildWebView() {
    if (!(Settings.writeRelatory === "html" || Settings.writeRelatory === true)) return;

    Handlebars.registerHelper('json', function(ctx) {
      return JSON.stringify(ctx);
    });

    const templateHTMLPath = path.join(__dirname, 'public', 'index.html');
    const outputPath = path.join('BP/', 'enderchest_webview.html');

    const contents = Array.from(EnderChestContent.getContent().values()).map(content => ({
      id: content._id,
      fullFilePath: content.filePath,
      filePath: path.basename(content.filePath),
      encryptedFilePath: path.basename(content.encryptedFilePath),
      dataSize: content.data.length,
      data: content.data
    }));
 
    // Template Handlebars
    let template = fs.readFileSync(templateHTMLPath, { encoding: 'utf-8' });
    template = this.#mergeJSandCSS(template);
    
    const compiled = Handlebars.compile(template);
    const html = compiled({ contents });

    fs.writeFileSync(outputPath, html.trim());

    Logger.info("The Webview was generated on the Behavior Pack root output on the file \"enderchest_webview.html\"");
  }

  /**
   * Merge CSS and JS files into HTML template. This is just to avoid webpack for just this.
   * @param {string} templateHTML The template HTML file.
   * @returns The merged stringfied version of the template file.
   */
  static #mergeJSandCSS(templateHTML) {
    const scriptsPath = path.join(__dirname, 'public', 'scripts.js');
    const scriptsContent = fs.readFileSync(scriptsPath, 'utf-8');

    const cssPath = path.join(__dirname, 'public', 'styles.css');
    const cssContent = fs.readFileSync(cssPath, 'utf-8');

    return templateHTML
                    .replace(/<!--[\s\S]*?-->/g, '')
                    .replace('</head>', `<style>${cssContent}</style>\n</head>`)
                    .replace(/\/\*[\s\S]*?\*\//g, '')
                    .replace('</body>', `<script>${scriptsContent}</script>\n</body>`)
                    .replace(/\/\*[\s\S]*?\*\//g, '')
                    .replace(/\/\/.*$/gm, '')
                    .replace(/\s+/g, ' ');
  }

  static buildTextFile() {
    if (!(Settings.writeRelatory === "json" || Settings.writeRelatory === true)) return;

    const filePath = path.join('BP/', 'enderchest.json');

    fs.writeFileSync(filePath, JSON.stringify(EnderChestContent.getParsedJSON(), null, 2), { encoding: 'utf-8' });
    Logger.info("The Text Fiule was generated on the Behavior Pack root output on the file \"enderchest_webview.html\"");
  }
}