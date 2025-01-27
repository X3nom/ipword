# IPWORD
IPWORD is tool for translation of ipv6 adresses into a human readable form and back.

## Usage
It's simple!
```bash
$ ipword <ipv6-address/word-address>
```
The tool will automatically decide if the parameter is ipv6 or words and will convert to the other representation of address.

### Example
```bash
$ ipword 2001:db8::8a2e:370:7334
cabal:auricle::mentum:afreet:jamboree

$ ipword cabal:auricle::mentum:afreet:jamboree
2001:db8::8a2e:370:7334
```



## Dictionary
The source dictionary used is http://www.webplaces.org/passwords/lists/hexadecimal-65536-list.txt
