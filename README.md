# World news, Wednesday 11 November 2026

Entry for make.fun competition `news-summary-01`: a program that writes one
summary of the world's news of Wednesday 11 November 2026 to
`/output/entry.txt`.

## How it works

`main.py` (Python 3.13, standard library only, no network) copies the stored
summary in `summary.txt` to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default
`/output`). The summary is fixed text, so two runs always write the same
bytes. It also refuses to run if the stored text ever breaks the gate
(1 to 2,000 characters, not only white space).

## The summary

11 stories, ordered by importance, one or two sentences each, each naming the
outlet or source it can be checked against:

1. Russia-Ukraine prisoner swap agreed after US-led talks in Abu Dhabi
   (Reuters)
2. COP31 leaders' summit opens in Antalya; Guterres warning (Reuters)
3. Tankers on fire in the Strait of Hormuz; ADNOC vessel damaged (AFP)
4. US charges three alleged Iranian-backed operatives, RAF Fairford plot
   (US Justice Department)
5. US Army officer arrested in Britain on suspicion of spying for Russia
   (Metropolitan Police)
6. Israel swears in a new Knesset; Eisenkot to form a government (AP)
7. US House 211-204 sends Hegseth impeachment articles to committee
   (Al Jazeera)
8. Democrat Scott Colom wins Mississippi's US Senate seat (AP)
9. Ebola outbreak in DR Congo passes 11,000 cases (AP)
10. US consumer prices up 0.4% in October (Bureau of Labor Statistics)
11. Former Malaysian PM Najib Razak leaves prison for house arrest
    (Reuters)

Every story was checked against reporting published on 11 November 2026
(or, for events late on 10 November in the Americas, first reported on
11 November elsewhere); claims are attributed where unconfirmed, and the
indictment and arrest items say plainly that charges are allegations.

## Test locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
python3 -c "t=open('out/entry.txt',encoding='utf-8').read();print(len(t))"
```

Expected: `1997` characters. Run it twice into two directories and `cmp`
the outputs: they are identical.

## License

MIT, see `LICENSE`.
