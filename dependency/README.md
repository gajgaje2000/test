# ⚡ Terminal Commands Cheatsheet

| Usage | PowerShell (VS Code Terminal) | Command Prompt (CMD) |
| :--- | :--- | :--- |
| **Clone repo into current folder** | `git clone --depth 1 https://github.com/gajgaje2000/test.git "filepath"` | `git clone --depth 1 https://github.com/gajgaje2000/test.git "filepath"` |
| **Copy folder (`dependency` -> `public`)** | `cp -r dependency webapp\public` | `robocopy dependency webapp\public /E` |
| **Delete folder (`node_modules`)** | `rm -r -fo node_modules` | `rd /s /q node_modules` |
| **Copy file to clipboard (`server.js`)** | `cat webapp\server.js \| clip` | `clip < webapp\server.js` |
| **Open file(Just like `Ctrl+O`) (`server.js`)** | `code "filepath"` | `code "filepath"` |
