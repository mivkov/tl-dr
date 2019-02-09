# Legalies
https://tlng-dr.herokuapp.com/

We've all seen it: huge blocks of dense text that pop up before you install a new piece of software or sign up for a new service. These days, End User License Agreements are everywhere but most of the time are too long and full of jargon for consumers to feasibly read. But no more! Our application, Legalies, finds the most notable sections of such a legal document — namely, sections which seem unusual and do not align with typical EULAs — and compiles them into a brief summary. Users cannot reasonably be expected to read dozens of pages of text for every product they use, but we hope to help prevent people from inadvertently agreeing to dubious privacy violations and signing away their rights.

**tl;dr:** what haven't you been reading in the Terms of Services you agree to?

### Installing the Chrome extension:

Visit chrome://extensions/, click the "Load Unpacked" button, and select the ```extensions``` folder when prompted.

### To use the Chrome extension:

Highlight your target text, right-click and select "Simplify" in the context menu. The summary should appear in the bottom-right corner of your screen.

## Built With

- [Flask](http://flask.pocoo.org/docs/1.0/)
- [Natural Language Toolkit (NLTK)](https://www.nltk.org/index.html)
- [scikit learn](https://scikit-learn.org/stable/documentation.html)
