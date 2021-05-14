# Rigol-rof-to-csv Python script
## Usage

Outputting data directly to stdout
```
python readROF.py infile.ROF
```

Saving output to csv file
```
python readROF.py infile.ROF > outfile.csv
```

Idea came from:
https://github.com/mcmayer/rigol-rof-reader

Format is documented in:
https://sigrok.org/wiki/File_format:Rigol_rof

## File format definition:
```
cccc    0 - 3	File identification, consisting of the letters "ROF" and a zero padding (52 4f 46 00)
c       4	unknown (always 01 so far)
c       5	unknown (61, 6e, 38)
h       6 - 7	Length of metadata header, little-endian (0c 00 00 00)
I       8 - 11	Always 0x00
h       12 - 13	Header CRC?
h       14 - 15	Data CRC?
```
Metadata header
```
h       16 - 19	Sample period in seconds, little-endian
h       20 - 23	Number of points, little-endian
h       24 - 27	Same as number of points.
```
The timespan of the file can be determined by:

sample period in seconds * number of points
Data
The data following the header consists of a number of points, where each of these is structured like this:

Bytes | Field
------|------
0 - 3 | Voltage, little-endian, times 10000
4 - 7 | Current, little-endian, times 10000

Example
```
(b'R', b'O', b'F', b'\x00', b'\x01', b'\xa3', 12, 0, 0, 19140, 1, 4000, 1952)
```

