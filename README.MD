mcsum
=====

Calcola il checksum di ogni riga di un programma BASIC per il C64. In questo modo è possibile verificare che quanto digitato corrisponda effettivamente al listato pubblicato sulla rivista [MC Microcomputer](http://www.mc-online.it/). 

L'algoritmo è descritto nell'articolo ["Un programma di CHECKSUM per i lettori"](https://archive.org/stream/MC_microcomputer-044/#page/n159/mode/2up) (MC Microcomputer n.44 pag. 161) e funziona in modo analogo al programma per C64 realizzato da Giancarlo Pezzé e distribuito anche nel [disco 1](http://ready64.org/download/scheda_download.php?id_download=826) de "Il meglio del software pubblicato su MC Microcomputer".

Su C64 Wiki è spiegato [come viene tokenizzato](https://www.c64-wiki.com/wiki/BASIC_token) un programma BASIC.

Se avete fatto l'OCR di un listato, potete rimuovere il checksum con il seguente comando:

	$ sed -i.bak -r 's/:[0-9]+$//' rem_in_reverse.txt

Dopodiché potete usare petcat per tokenizzare il programma:

	$ petcat -w2 -o rem_in_reverse.prg rem_in_reverse.txt

Infine potete calcolare il checksum di ogni riga e verificare che sia uguale a quello pubblicato:

	$ ./mcsum.py rem_in_reverse.prg

