# Tic-Tac-Toe Game Map (web)

Play tic-tac-toe in the browser and watch your game travel through a map of every possible ending.

**Play it:** https://mageshsridhar.github.io/tic-tac-toe-map-web/

Tic-tac-toe has 255,168 complete games, but if you treat rotations and reflections of the board as the same, they end on only **138 distinct finished boards**: 91 X wins, 44 O wins and 3 draws. The map follows your game from the empty board towards one of those 138.

## What it does

- **Play board:** a 3×3 board with pixel-art marks. It shows whose turn it is and the result of best play from the current position.
- **Game map:** each move travels down a branch to the next board. The boards you could reach next are shown as dashed options, each labelled with its best-play result and how many endings are still possible from it. Click an option to play it, or click an earlier board to go back.
- **Matching orientation:** many moves lead to the same position turned or mirrored. After a move on the board, a copy of the board turns to match the map's option and flies onto it, so the map never shows a board that looks different from yours without explaining why.
- **Endings legend:** one dot for each of the 138 endings. A dot stays lit while that ending is still reachable, and the ending you reach is circled.
- **Layouts:** a side-by-side layout for wide screens, a stacked one for upright tablets, and a compact phone layout where the board and map share one screen. On phones a finished game is shown as a grid.
- **Look and feel:** pastel light and dark themes with a bubble transition between them, and animated moves and undos. Reduce Motion is respected.

## How it works

The page solves the game with minimax over the 765 positions that remain once symmetric boards are merged. For each position it also records which of the 138 endings can still be reached. A board's canonical key is the smallest of its 8 rotations and reflections. The map is drawn with [D3.js](https://d3js.org).

## Files

- `template.html`: the page source.
- `endings.json`: the 138 finished boards.
- `build.py`: combines the two into `index.html`, a single self-contained page. GitHub Pages serves `index.html`.

After editing `template.html`, rebuild the page:

```bash
python3 build.py
```

To try it locally:

```bash
python3 -m http.server 8000
```

Then open http://localhost:8000.

The iPad version, built with SwiftUI, is in [tic-tac-toe-map](https://github.com/mageshsridhar/tic-tac-toe-map).
