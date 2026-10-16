# Figuras

`arquitetura.png` (3280×2040) — diagrama da arquitetura multiagente, para os slides.
`arquitetura.svg` — fonte editável do diagrama.

Para regerar o PNG depois de editar o SVG (precisa do Chrome):

```powershell
& "C:\Program Files\Google\Chrome\Application\chrome.exe" --headless=new --disable-gpu `
  --force-device-scale-factor=2 --window-size=1640,1020 --default-background-color=ffffffff `
  --screenshot="$PWD\arquitetura.png" "$PWD\render.html"
```
