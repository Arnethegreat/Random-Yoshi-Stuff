; Jump table base: $02A9B7  bank: $02
;  Sprite |  X reg | Ptr addr | Ptr val |   Target |        Kind | Safe |             Zone | Notes
;    $0000 |    $BC |  $02AA73 |   $4299 |  $024299 |      RAM/IO |      |            table | -> I/O $4299
;    $0001 |    $BE |  $02AA75 |   $B975 |  $02B975 |         ROM |      |            table | 
;    $0002 |    $C0 |  $02AA77 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0003 |    $C2 |  $02AA79 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $0004 |    $C4 |  $02AA7B |   $99FF |  $0299FF |         ROM |      |            table | 
;    $0005 |    $C6 |  $02AA7D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0006 |    $C8 |  $02AA7F |   $02C6 |  $0202C6 |  RAM-mirror |      |            table | -> $7E02C6
;    $0007 |    $CA |  $02AA81 |   $BED0 |  $02BED0 |         ROM |      |            table | 
;    $0008 |    $CC |  $02AA83 |   $214C |  $02214C |      RAM/IO |      |            table | -> I/O $214C
;    $0009 |    $CE |  $02AA85 |   $BBAA |  $02BBAA |         ROM | direct RTS |            table | 
;    $000A |    $D0 |  $02AA87 |   $DEAD |  $02DEAD |         ROM |      |            table | 
;    $000B |    $D2 |  $02AA89 |   $D060 |  $02D060 |         ROM |      |            table | 
;    $000C |    $D4 |  $02AA8B |   $A97D |  $02A97D |         ROM |      |            table | 
;    $000D |    $D6 |  $02AA8D |   $0002 |  $020002 |  RAM-mirror |      |            table | -> $7E0002
;    $000E |    $D8 |  $02AA8F |   $AC8D |  $02AC8D |         ROM |      |            table | 
;    $000F |    $DA |  $02AA91 |   $9C60 |  $029C60 |         ROM |      |            table | 
;    $0010 |    $DC |  $02AA93 |   $617A |  $02617A | SRAM-mirror |      |            table | -> SRAM $017A
;    $0011 |    $DE |  $02AA95 |   $7C9C |  $027C9C | SRAM-mirror |      |            table | -> SRAM $1C9C
;    $0012 |    $E0 |  $02AA97 |   $F661 |  $02F661 |         ROM |      |            table | 
;    $0013 |    $E2 |  $02AA99 |   $A918 |  $02A918 |         ROM |      |            table | 
;    $0014 |    $E4 |  $02AA9B |   $0054 |  $020054 |  RAM-mirror |      |            table | -> $7E0054
;    $0015 |    $E6 |  $02AA9D |   $969D |  $02969D |         ROM |      |            table | 
;    $0016 |    $E8 |  $02AA9F |   $A07A |  $02A07A |         ROM |      |            table | 
;    $0017 |    $EA |  $02AAA1 |   $A904 |  $02A904 |         ROM |      |            table | 
;    $0018 |    $EC |  $02AAA3 |   $008C |  $02008C |  RAM-mirror |      |            table | -> $7E008C
;    $0019 |    $EE |  $02AAA5 |   $4E22 |  $024E22 |      RAM/IO |      |            table | -> I/O $4E22
;    $001A |    $F0 |  $02AAA7 |   $03A3 |  $0203A3 |  RAM-mirror |      |            table | -> $7E03A3
;    $001B |    $F2 |  $02AAA9 |   $1A98 |  $021A98 |  RAM-mirror |      |            table | -> $7E1A98
;    $001C |    $F4 |  $02AAAB |   $369D |  $02369D |      RAM/IO |      |            table | -> I/O $369D
;    $001D |    $F6 |  $02AAAD |   $AD7A |  $02AD7A |         ROM |      |            table | 
;    $001E |    $F8 |  $02AAAF |   $608C |  $02608C | SRAM-mirror |      |            table | -> SRAM $008C
;    $001F |    $FA |  $02AAB1 |   $E299 |  $02E299 |         ROM |      |            table | 
;    $0020 |    $FC |  $02AAB3 |   $AD70 |  $02AD70 |         ROM |      |            table | 
;    $0021 |    $FE |  $02AAB5 |   $6090 |  $026090 | SRAM-mirror |      |            table | -> SRAM $0090
;    $0022 |    $00 |  $02A9B7 |   $A9CB |  $02A9CB |         ROM | valid table |      intentional | 
;    $0023 |    $02 |  $02A9B9 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $0024 |    $04 |  $02A9BB |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $0025 |    $06 |  $02A9BD |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $0026 |    $08 |  $02A9BF |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $0027 |    $0A |  $02A9C1 |   $AA20 |  $02AA20 |         ROM | valid table |      intentional | 
;    $0028 |    $0C |  $02A9C3 |   $AA2A |  $02AA2A |         ROM | valid table |      intentional | 
;    $0029 |    $0E |  $02A9C5 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $002A |    $10 |  $02A9C7 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $002B |    $12 |  $02A9C9 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $002C |    $14 |  $02A9CB |   $BDBB |  $02BDBB |         ROM |      |            table | 
;    $002D |    $16 |  $02A9CD |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $002E |    $18 |  $02A9CF |   $008D |  $02008D |  RAM-mirror |      |            table | -> $7E008D
;    $002F |    $1A |  $02A9D1 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $0030 |    $1C |  $02A9D3 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
;    $0031 |    $1E |  $02A9D5 |   $028D |  $02028D |  RAM-mirror |      |            table | -> $7E028D
;    $0032 |    $20 |  $02A9D7 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $0033 |    $22 |  $02A9D9 |   $7042 |  $027042 | SRAM-mirror |      |            table | -> SRAM $1042
;    $0034 |    $24 |  $02A9DB |   $048D |  $02048D |  RAM-mirror |      |            table | -> $7E048D
;    $0035 |    $26 |  $02A9DD |   $DA00 |  $02DA00 |         ROM |      |            table | 
;    $0036 |    $28 |  $02A9DF |   $8E22 |  $028E22 |         ROM |      |            table | 
;    $0037 |    $2A |  $02A9E1 |   $04F8 |  $0204F8 |  RAM-mirror |      |            table | -> $7E04F8
;    $0038 |    $2C |  $02A9E3 |   $A9FA |  $02A9FA |         ROM |      |            table | 
;    $0039 |    $2E |  $02A9E5 |   $0006 |  $020006 |  RAM-mirror |      |            table | -> $7E0006
;    $003A |    $30 |  $02A9E7 |   $2248 |  $022248 |      RAM/IO |      |            table | -> I/O $2248
;    $003B |    $32 |  $02A9E9 |   $BF87 |  $02BF87 |         ROM |      |            table | 
;    $003C |    $34 |  $02A9EB |   $A903 |  $02A903 |         ROM |      |            table | 
;    $003D |    $36 |  $02A9ED |   $0115 |  $020115 |  RAM-mirror |      |            table | -> $7E0115
;    $003E |    $38 |  $02A9EF |   $229B |  $02229B |      RAM/IO |      |            table | -> I/O $229B
;    $003F |    $3A |  $02A9F1 |   $A377 |  $02A377 |         ROM |      |            table | 
;    $0040 |    $3C |  $02A9F3 |   $6803 |  $026803 | SRAM-mirror |      |            table | -> SRAM $0803
;    $0041 |    $3E |  $02A9F5 |   $425D |  $02425D |      RAM/IO |      |            table | -> I/O $425D
;    $0042 |    $40 |  $02A9F7 |   $9D70 |  $029D70 |         ROM |      |            table | 
;    $0043 |    $42 |  $02A9F9 |   $7042 |  $027042 | SRAM-mirror |      |            table | -> SRAM $1042
;    $0044 |    $44 |  $02A9FB |   $30A9 |  $0230A9 |      RAM/IO |      |            table | -> I/O $30A9
;    $0045 |    $46 |  $02A9FD |   $9D00 |  $029D00 |         ROM |      |            table | 
;    $0046 |    $48 |  $02A9FF |   $7A96 |  $027A96 | SRAM-mirror |      |            table | -> SRAM $1A96
;    $0047 |    $4A |  $02AA01 |   $989D |  $02989D |         ROM |      |            table | 
;    $0048 |    $4C |  $02AA03 |   $9D7A |  $029D7A |         ROM |      |            table | 
;    $0049 |    $4E |  $02AA05 |   $7AF6 |  $027AF6 | SRAM-mirror |      |            table | -> SRAM $1AF6
;    $004A |    $50 |  $02AA07 |   $D89D |  $02D89D |         ROM |      |            table | 
;    $004B |    $52 |  $02AA09 |   $A979 |  $02A979 |         ROM |      |            table | 
;    $004C |    $54 |  $02AA0B |   $FE80 |  $02FE80 |         ROM |      |            table | 
;    $004D |    $56 |  $02AA0D |   $229D |  $02229D |      RAM/IO |      |            table | -> I/O $229D
;    $004E |    $58 |  $02AA0F |   $A972 |  $02A972 |         ROM |      |            table | 
;    $004F |    $5A |  $02AA11 |   $0008 |  $020008 |  RAM-mirror |      |            table | -> $7E0008
;    $0050 |    $5C |  $02AA13 |   $429D |  $02429D |      RAM/IO |      |            table | -> I/O $429D
;    $0051 |    $5E |  $02AA15 |   $BD75 |  $02BD75 |         ROM |      |            table | 
;    $0052 |    $60 |  $02AA17 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0053 |    $62 |  $02AA19 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $0054 |    $64 |  $02AA1B |   $9DFF |  $029DFF |         ROM |      |            table | 
;    $0055 |    $66 |  $02AA1D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0056 |    $68 |  $02AA1F |   $BB60 |  $02BB60 |         ROM |      |            table | 
;    $0057 |    $6A |  $02AA21 |   $F422 |  $02F422 |         ROM |      |            table | 
;    $0058 |    $6C |  $02AA23 |   $02A4 |  $0202A4 |  RAM-mirror |      |            table | -> $7E02A4
;    $0059 |    $6E |  $02AA25 |   $00A9 |  $0200A9 |  RAM-mirror |      |            table | -> $7E00A9
;    $005A |    $70 |  $02AA27 |   $8000 |  $028000 |         ROM |      |            table | 
;    $005B |    $72 |  $02AA29 |   $BBBD |  $02BBBD |         ROM |      |            table | 
;    $005C |    $74 |  $02AA2B |   $8722 |  $028722 |         ROM |      |            table | 
;    $005D |    $76 |  $02AA2D |   $03BF |  $0203BF |  RAM-mirror |      |            table | -> $7E03BF
;    $005E |    $78 |  $02AA2F |   $00A9 |  $0200A9 |  RAM-mirror |      |            table | -> $7E00A9
;    $005F |    $7A |  $02AA31 |   $9DFB |  $029DFB |         ROM |      |            table | 
;    $0060 |    $7C |  $02AA33 |   $7222 |  $027222 | SRAM-mirror |      |            table | -> SRAM $1222
;    $0061 |    $7E |  $02AA35 |   $BB60 |  $02BB60 |         ROM |      |            table | 
;    $0062 |    $80 |  $02AA37 |   $82BD |  $0282BD |         ROM |      |            table | 
;    $0063 |    $82 |  $02AA39 |   $8571 |  $028571 |         ROM |      |            table | 
;    $0064 |    $84 |  $02AA3B |   $A900 |  $02A900 |         ROM |      |            table | 
;    $0065 |    $86 |  $02AA3D |   $0003 |  $020003 |  RAM-mirror |      |            table | -> $7E0003
;    $0066 |    $88 |  $02AA3F |   $0285 |  $020285 |  RAM-mirror |      |            table | -> $7E0285
;    $0067 |    $8A |  $02AA41 |   $15A9 |  $0215A9 |  RAM-mirror |      |            table | -> $7E15A9
;    $0068 |    $8C |  $02AA43 |   $2201 |  $022201 |      RAM/IO |      |            table | -> I/O $2201
;    $0069 |    $8E |  $02AA45 |   $A364 |  $02A364 |         ROM |      |            table | 
;    $006A |    $90 |  $02AA47 |   $9003 |  $029003 |         ROM |      |            table | 
;    $006B |    $92 |  $02AA49 |   $BDD7 |  $02BDD7 |         ROM |      |            table | 
;    $006C |    $94 |  $02AA4B |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $006D |    $96 |  $02AA4D |   $E299 |  $02E299 |         ROM |      |            table | 
;    $006E |    $98 |  $02AA4F |   $A570 |  $02A570 |         ROM |      |            table | 
;    $006F |    $9A |  $02AA51 |   $3800 |  $023800 |      RAM/IO |      |            table | -> I/O $3800
;    $0070 |    $9C |  $02AA53 |   $10E9 |  $0210E9 |  RAM-mirror |      |            table | -> $7E10E9
;    $0071 |    $9E |  $02AA55 |   $9900 |  $029900 |         ROM |      |            table | 
;    $0072 |    $A0 |  $02AA57 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
;    $0073 |    $A2 |  $02AA59 |   $0085 |  $020085 |  RAM-mirror |      |            table | -> $7E0085
;    $0074 |    $A4 |  $02AA5B |   $30A9 |  $0230A9 |      RAM/IO |      |            table | -> I/O $30A9
;    $0075 |    $A6 |  $02AA5D |   $9900 |  $029900 |         ROM |      |            table | 
;    $0076 |    $A8 |  $02AA5F |   $7A96 |  $027A96 | SRAM-mirror |      |            table | -> SRAM $1A96
;    $0077 |    $AA |  $02AA61 |   $9899 |  $029899 |         ROM |      |            table | 
;    $0078 |    $AC |  $02AA63 |   $997A |  $02997A |         ROM |      |            table | 
;    $0079 |    $AE |  $02AA65 |   $7AF6 |  $027AF6 | SRAM-mirror |      |            table | -> SRAM $1AF6
;    $007A |    $B0 |  $02AA67 |   $D899 |  $02D899 |         ROM |      |            table | 
;    $007B |    $B2 |  $02AA69 |   $A979 |  $02A979 |         ROM |      |            table | 
;    $007C |    $B4 |  $02AA6B |   $FE80 |  $02FE80 |         ROM |      |            table | 
;    $007D |    $B6 |  $02AA6D |   $2299 |  $022299 |      RAM/IO |      |            table | -> I/O $2299
;    $007E |    $B8 |  $02AA6F |   $A972 |  $02A972 |         ROM |      |            table | 
;    $007F |    $BA |  $02AA71 |   $0008 |  $020008 |  RAM-mirror |      |            table | -> $7E0008
;    $0080 |    $BC |  $02AA73 |   $4299 |  $024299 |      RAM/IO |      |            table | -> I/O $4299
;    $0081 |    $BE |  $02AA75 |   $B975 |  $02B975 |         ROM |      |            table | 
;    $0082 |    $C0 |  $02AA77 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0083 |    $C2 |  $02AA79 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $0084 |    $C4 |  $02AA7B |   $99FF |  $0299FF |         ROM |      |            table | 
;    $0085 |    $C6 |  $02AA7D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0086 |    $C8 |  $02AA7F |   $02C6 |  $0202C6 |  RAM-mirror |      |            table | -> $7E02C6
;    $0087 |    $CA |  $02AA81 |   $BED0 |  $02BED0 |         ROM |      |            table | 
;    $0088 |    $CC |  $02AA83 |   $214C |  $02214C |      RAM/IO |      |            table | -> I/O $214C
;    $0089 |    $CE |  $02AA85 |   $BBAA |  $02BBAA |         ROM | direct RTS |            table | 
;    $008A |    $D0 |  $02AA87 |   $DEAD |  $02DEAD |         ROM |      |            table | 
;    $008B |    $D2 |  $02AA89 |   $D060 |  $02D060 |         ROM |      |            table | 
;    $008C |    $D4 |  $02AA8B |   $A97D |  $02A97D |         ROM |      |            table | 
;    $008D |    $D6 |  $02AA8D |   $0002 |  $020002 |  RAM-mirror |      |            table | -> $7E0002
;    $008E |    $D8 |  $02AA8F |   $AC8D |  $02AC8D |         ROM |      |            table | 
;    $008F |    $DA |  $02AA91 |   $9C60 |  $029C60 |         ROM |      |            table | 
;    $0090 |    $DC |  $02AA93 |   $617A |  $02617A | SRAM-mirror |      |            table | -> SRAM $017A
;    $0091 |    $DE |  $02AA95 |   $7C9C |  $027C9C | SRAM-mirror |      |            table | -> SRAM $1C9C
;    $0092 |    $E0 |  $02AA97 |   $F661 |  $02F661 |         ROM |      |            table | 
;    $0093 |    $E2 |  $02AA99 |   $A918 |  $02A918 |         ROM |      |            table | 
;    $0094 |    $E4 |  $02AA9B |   $0054 |  $020054 |  RAM-mirror |      |            table | -> $7E0054
;    $0095 |    $E6 |  $02AA9D |   $969D |  $02969D |         ROM |      |            table | 
;    $0096 |    $E8 |  $02AA9F |   $A07A |  $02A07A |         ROM |      |            table | 
;    $0097 |    $EA |  $02AAA1 |   $A904 |  $02A904 |         ROM |      |            table | 
;    $0098 |    $EC |  $02AAA3 |   $008C |  $02008C |  RAM-mirror |      |            table | -> $7E008C
;    $0099 |    $EE |  $02AAA5 |   $4E22 |  $024E22 |      RAM/IO |      |            table | -> I/O $4E22
;    $009A |    $F0 |  $02AAA7 |   $03A3 |  $0203A3 |  RAM-mirror |      |            table | -> $7E03A3
;    $009B |    $F2 |  $02AAA9 |   $1A98 |  $021A98 |  RAM-mirror |      |            table | -> $7E1A98
;    $009C |    $F4 |  $02AAAB |   $369D |  $02369D |      RAM/IO |      |            table | -> I/O $369D
;    $009D |    $F6 |  $02AAAD |   $AD7A |  $02AD7A |         ROM |      |            table | 
;    $009E |    $F8 |  $02AAAF |   $608C |  $02608C | SRAM-mirror |      |            table | -> SRAM $008C
;    $009F |    $FA |  $02AAB1 |   $E299 |  $02E299 |         ROM |      |            table | 
;    $00A0 |    $FC |  $02AAB3 |   $AD70 |  $02AD70 |         ROM |      |            table | 
;    $00A1 |    $FE |  $02AAB5 |   $6090 |  $026090 | SRAM-mirror |      |            table | -> SRAM $0090
;    $00A2 |    $00 |  $02A9B7 |   $A9CB |  $02A9CB |         ROM | valid table |      intentional | 
;    $00A3 |    $02 |  $02A9B9 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $00A4 |    $04 |  $02A9BB |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $00A5 |    $06 |  $02A9BD |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $00A6 |    $08 |  $02A9BF |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $00A7 |    $0A |  $02A9C1 |   $AA20 |  $02AA20 |         ROM | valid table |      intentional | 
;    $00A8 |    $0C |  $02A9C3 |   $AA2A |  $02AA2A |         ROM | valid table |      intentional | 
;    $00A9 |    $0E |  $02A9C5 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $00AA |    $10 |  $02A9C7 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $00AB |    $12 |  $02A9C9 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $00AC |    $14 |  $02A9CB |   $BDBB |  $02BDBB |         ROM |      |            table | 
;    $00AD |    $16 |  $02A9CD |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $00AE |    $18 |  $02A9CF |   $008D |  $02008D |  RAM-mirror |      |            table | -> $7E008D
;    $00AF |    $1A |  $02A9D1 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $00B0 |    $1C |  $02A9D3 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
;    $00B1 |    $1E |  $02A9D5 |   $028D |  $02028D |  RAM-mirror |      |            table | -> $7E028D
;    $00B2 |    $20 |  $02A9D7 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $00B3 |    $22 |  $02A9D9 |   $7042 |  $027042 | SRAM-mirror |      |            table | -> SRAM $1042
;    $00B4 |    $24 |  $02A9DB |   $048D |  $02048D |  RAM-mirror |      |            table | -> $7E048D
;    $00B5 |    $26 |  $02A9DD |   $DA00 |  $02DA00 |         ROM |      |            table | 
;    $00B6 |    $28 |  $02A9DF |   $8E22 |  $028E22 |         ROM |      |            table | 
;    $00B7 |    $2A |  $02A9E1 |   $04F8 |  $0204F8 |  RAM-mirror |      |            table | -> $7E04F8
;    $00B8 |    $2C |  $02A9E3 |   $A9FA |  $02A9FA |         ROM |      |            table | 
;    $00B9 |    $2E |  $02A9E5 |   $0006 |  $020006 |  RAM-mirror |      |            table | -> $7E0006
;    $00BA |    $30 |  $02A9E7 |   $2248 |  $022248 |      RAM/IO |      |            table | -> I/O $2248
;    $00BB |    $32 |  $02A9E9 |   $BF87 |  $02BF87 |         ROM |      |            table | 
;    $00BC |    $34 |  $02A9EB |   $A903 |  $02A903 |         ROM |      |            table | 
;    $00BD |    $36 |  $02A9ED |   $0115 |  $020115 |  RAM-mirror |      |            table | -> $7E0115
;    $00BE |    $38 |  $02A9EF |   $229B |  $02229B |      RAM/IO |      |            table | -> I/O $229B
;    $00BF |    $3A |  $02A9F1 |   $A377 |  $02A377 |         ROM |      |            table | 
;    $00C0 |    $3C |  $02A9F3 |   $6803 |  $026803 | SRAM-mirror |      |            table | -> SRAM $0803
;    $00C1 |    $3E |  $02A9F5 |   $425D |  $02425D |      RAM/IO |      |            table | -> I/O $425D
;    $00C2 |    $40 |  $02A9F7 |   $9D70 |  $029D70 |         ROM |      |            table | 
;    $00C3 |    $42 |  $02A9F9 |   $7042 |  $027042 | SRAM-mirror |      |            table | -> SRAM $1042
;    $00C4 |    $44 |  $02A9FB |   $30A9 |  $0230A9 |      RAM/IO |      |            table | -> I/O $30A9
;    $00C5 |    $46 |  $02A9FD |   $9D00 |  $029D00 |         ROM |      |            table | 
;    $00C6 |    $48 |  $02A9FF |   $7A96 |  $027A96 | SRAM-mirror |      |            table | -> SRAM $1A96
;    $00C7 |    $4A |  $02AA01 |   $989D |  $02989D |         ROM |      |            table | 
;    $00C8 |    $4C |  $02AA03 |   $9D7A |  $029D7A |         ROM |      |            table | 
;    $00C9 |    $4E |  $02AA05 |   $7AF6 |  $027AF6 | SRAM-mirror |      |            table | -> SRAM $1AF6
;    $00CA |    $50 |  $02AA07 |   $D89D |  $02D89D |         ROM |      |            table | 
;    $00CB |    $52 |  $02AA09 |   $A979 |  $02A979 |         ROM |      |            table | 
;    $00CC |    $54 |  $02AA0B |   $FE80 |  $02FE80 |         ROM |      |            table | 
;    $00CD |    $56 |  $02AA0D |   $229D |  $02229D |      RAM/IO |      |            table | -> I/O $229D
;    $00CE |    $58 |  $02AA0F |   $A972 |  $02A972 |         ROM |      |            table | 
;    $00CF |    $5A |  $02AA11 |   $0008 |  $020008 |  RAM-mirror |      |            table | -> $7E0008
;    $00D0 |    $5C |  $02AA13 |   $429D |  $02429D |      RAM/IO |      |            table | -> I/O $429D
;    $00D1 |    $5E |  $02AA15 |   $BD75 |  $02BD75 |         ROM |      |            table | 
;    $00D2 |    $60 |  $02AA17 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $00D3 |    $62 |  $02AA19 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $00D4 |    $64 |  $02AA1B |   $9DFF |  $029DFF |         ROM |      |            table | 
;    $00D5 |    $66 |  $02AA1D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $00D6 |    $68 |  $02AA1F |   $BB60 |  $02BB60 |         ROM |      |            table | 
;    $00D7 |    $6A |  $02AA21 |   $F422 |  $02F422 |         ROM |      |            table | 
;    $00D8 |    $6C |  $02AA23 |   $02A4 |  $0202A4 |  RAM-mirror |      |            table | -> $7E02A4
;    $00D9 |    $6E |  $02AA25 |   $00A9 |  $0200A9 |  RAM-mirror |      |            table | -> $7E00A9
;    $00DA |    $70 |  $02AA27 |   $8000 |  $028000 |         ROM |      |            table | 
;    $00DB |    $72 |  $02AA29 |   $BBBD |  $02BBBD |         ROM |      |            table | 
;    $00DC |    $74 |  $02AA2B |   $8722 |  $028722 |         ROM |      |            table | 
;    $00DD |    $76 |  $02AA2D |   $03BF |  $0203BF |  RAM-mirror |      |            table | -> $7E03BF
;    $00DE |    $78 |  $02AA2F |   $00A9 |  $0200A9 |  RAM-mirror |      |            table | -> $7E00A9
;    $00DF |    $7A |  $02AA31 |   $9DFB |  $029DFB |         ROM |      |            table | 
;    $00E0 |    $7C |  $02AA33 |   $7222 |  $027222 | SRAM-mirror |      |            table | -> SRAM $1222
;    $00E1 |    $7E |  $02AA35 |   $BB60 |  $02BB60 |         ROM |      |            table | 
;    $00E2 |    $80 |  $02AA37 |   $82BD |  $0282BD |         ROM |      |            table | 
;    $00E3 |    $82 |  $02AA39 |   $8571 |  $028571 |         ROM |      |            table | 
;    $00E4 |    $84 |  $02AA3B |   $A900 |  $02A900 |         ROM |      |            table | 
;    $00E5 |    $86 |  $02AA3D |   $0003 |  $020003 |  RAM-mirror |      |            table | -> $7E0003
;    $00E6 |    $88 |  $02AA3F |   $0285 |  $020285 |  RAM-mirror |      |            table | -> $7E0285
;    $00E7 |    $8A |  $02AA41 |   $15A9 |  $0215A9 |  RAM-mirror |      |            table | -> $7E15A9
;    $00E8 |    $8C |  $02AA43 |   $2201 |  $022201 |      RAM/IO |      |            table | -> I/O $2201
;    $00E9 |    $8E |  $02AA45 |   $A364 |  $02A364 |         ROM |      |            table | 
;    $00EA |    $90 |  $02AA47 |   $9003 |  $029003 |         ROM |      |            table | 
;    $00EB |    $92 |  $02AA49 |   $BDD7 |  $02BDD7 |         ROM |      |            table | 
;    $00EC |    $94 |  $02AA4B |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $00ED |    $96 |  $02AA4D |   $E299 |  $02E299 |         ROM |      |            table | 
;    $00EE |    $98 |  $02AA4F |   $A570 |  $02A570 |         ROM |      |            table | 
;    $00EF |    $9A |  $02AA51 |   $3800 |  $023800 |      RAM/IO |      |            table | -> I/O $3800
;    $00F0 |    $9C |  $02AA53 |   $10E9 |  $0210E9 |  RAM-mirror |      |            table | -> $7E10E9
;    $00F1 |    $9E |  $02AA55 |   $9900 |  $029900 |         ROM |      |            table | 
;    $00F2 |    $A0 |  $02AA57 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
;    $00F3 |    $A2 |  $02AA59 |   $0085 |  $020085 |  RAM-mirror |      |            table | -> $7E0085
;    $00F4 |    $A4 |  $02AA5B |   $30A9 |  $0230A9 |      RAM/IO |      |            table | -> I/O $30A9
;    $00F5 |    $A6 |  $02AA5D |   $9900 |  $029900 |         ROM |      |            table | 
;    $00F6 |    $A8 |  $02AA5F |   $7A96 |  $027A96 | SRAM-mirror |      |            table | -> SRAM $1A96
;    $00F7 |    $AA |  $02AA61 |   $9899 |  $029899 |         ROM |      |            table | 
;    $00F8 |    $AC |  $02AA63 |   $997A |  $02997A |         ROM |      |            table | 
;    $00F9 |    $AE |  $02AA65 |   $7AF6 |  $027AF6 | SRAM-mirror |      |            table | -> SRAM $1AF6
;    $00FA |    $B0 |  $02AA67 |   $D899 |  $02D899 |         ROM |      |            table | 
;    $00FB |    $B2 |  $02AA69 |   $A979 |  $02A979 |         ROM |      |            table | 
;    $00FC |    $B4 |  $02AA6B |   $FE80 |  $02FE80 |         ROM |      |            table | 
;    $00FD |    $B6 |  $02AA6D |   $2299 |  $022299 |      RAM/IO |      |            table | -> I/O $2299
;    $00FE |    $B8 |  $02AA6F |   $A972 |  $02A972 |         ROM |      |            table | 
;    $00FF |    $BA |  $02AA71 |   $0008 |  $020008 |  RAM-mirror |      |            table | -> $7E0008
;    $0100 |    $BC |  $02AA73 |   $4299 |  $024299 |      RAM/IO |      |            table | -> I/O $4299
;    $0101 |    $BE |  $02AA75 |   $B975 |  $02B975 |         ROM |      |            table | 
;    $0102 |    $C0 |  $02AA77 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0103 |    $C2 |  $02AA79 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $0104 |    $C4 |  $02AA7B |   $99FF |  $0299FF |         ROM |      |            table | 
;    $0105 |    $C6 |  $02AA7D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0106 |    $C8 |  $02AA7F |   $02C6 |  $0202C6 |  RAM-mirror |      |            table | -> $7E02C6
;    $0107 |    $CA |  $02AA81 |   $BED0 |  $02BED0 |         ROM |      |            table | 
;    $0108 |    $CC |  $02AA83 |   $214C |  $02214C |      RAM/IO |      |            table | -> I/O $214C
;    $0109 |    $CE |  $02AA85 |   $BBAA |  $02BBAA |         ROM | direct RTS |            table | 
;    $010A |    $D0 |  $02AA87 |   $DEAD |  $02DEAD |         ROM |      |            table | 
;    $010B |    $D2 |  $02AA89 |   $D060 |  $02D060 |         ROM |      |            table | 
;    $010C |    $D4 |  $02AA8B |   $A97D |  $02A97D |         ROM |      |            table | 
;    $010D |    $D6 |  $02AA8D |   $0002 |  $020002 |  RAM-mirror |      |            table | -> $7E0002
;    $010E |    $D8 |  $02AA8F |   $AC8D |  $02AC8D |         ROM |      |            table | 
;    $010F |    $DA |  $02AA91 |   $9C60 |  $029C60 |         ROM |      |            table | 
;    $0110 |    $DC |  $02AA93 |   $617A |  $02617A | SRAM-mirror |      |            table | -> SRAM $017A
;    $0111 |    $DE |  $02AA95 |   $7C9C |  $027C9C | SRAM-mirror |      |            table | -> SRAM $1C9C
;    $0112 |    $E0 |  $02AA97 |   $F661 |  $02F661 |         ROM |      |            table | 
;    $0113 |    $E2 |  $02AA99 |   $A918 |  $02A918 |         ROM |      |            table | 
;    $0114 |    $E4 |  $02AA9B |   $0054 |  $020054 |  RAM-mirror |      |            table | -> $7E0054
;    $0115 |    $E6 |  $02AA9D |   $969D |  $02969D |         ROM |      |            table | 
;    $0116 |    $E8 |  $02AA9F |   $A07A |  $02A07A |         ROM |      |            table | 
;    $0117 |    $EA |  $02AAA1 |   $A904 |  $02A904 |         ROM |      |            table | 
;    $0118 |    $EC |  $02AAA3 |   $008C |  $02008C |  RAM-mirror |      |            table | -> $7E008C
;    $0119 |    $EE |  $02AAA5 |   $4E22 |  $024E22 |      RAM/IO |      |            table | -> I/O $4E22
;    $011A |    $F0 |  $02AAA7 |   $03A3 |  $0203A3 |  RAM-mirror |      |            table | -> $7E03A3
;    $011B |    $F2 |  $02AAA9 |   $1A98 |  $021A98 |  RAM-mirror |      |            table | -> $7E1A98
;    $011C |    $F4 |  $02AAAB |   $369D |  $02369D |      RAM/IO |      |            table | -> I/O $369D
;    $011D |    $F6 |  $02AAAD |   $AD7A |  $02AD7A |         ROM |      |            table | 
;    $011E |    $F8 |  $02AAAF |   $608C |  $02608C | SRAM-mirror |      |            table | -> SRAM $008C
;    $011F |    $FA |  $02AAB1 |   $E299 |  $02E299 |         ROM |      |            table | 
;    $0120 |    $FC |  $02AAB3 |   $AD70 |  $02AD70 |         ROM |      |            table | 
;    $0121 |    $FE |  $02AAB5 |   $6090 |  $026090 | SRAM-mirror |      |            table | -> SRAM $0090
;    $0122 |    $00 |  $02A9B7 |   $A9CB |  $02A9CB |         ROM | valid table |      intentional | 
;    $0123 |    $02 |  $02A9B9 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $0124 |    $04 |  $02A9BB |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $0125 |    $06 |  $02A9BD |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $0126 |    $08 |  $02A9BF |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $0127 |    $0A |  $02A9C1 |   $AA20 |  $02AA20 |         ROM | valid table |      intentional | 
;    $0128 |    $0C |  $02A9C3 |   $AA2A |  $02AA2A |         ROM | valid table |      intentional | 
;    $0129 |    $0E |  $02A9C5 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $012A |    $10 |  $02A9C7 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $012B |    $12 |  $02A9C9 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $012C |    $14 |  $02A9CB |   $BDBB |  $02BDBB |         ROM |      |            table | 
;    $012D |    $16 |  $02A9CD |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $012E |    $18 |  $02A9CF |   $008D |  $02008D |  RAM-mirror |      |            table | -> $7E008D
;    $012F |    $1A |  $02A9D1 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $0130 |    $1C |  $02A9D3 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
;    $0131 |    $1E |  $02A9D5 |   $028D |  $02028D |  RAM-mirror |      |            table | -> $7E028D
;    $0132 |    $20 |  $02A9D7 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $0133 |    $22 |  $02A9D9 |   $7042 |  $027042 | SRAM-mirror |      |            table | -> SRAM $1042
;    $0134 |    $24 |  $02A9DB |   $048D |  $02048D |  RAM-mirror |      |            table | -> $7E048D
;    $0135 |    $26 |  $02A9DD |   $DA00 |  $02DA00 |         ROM |      |            table | 
;    $0136 |    $28 |  $02A9DF |   $8E22 |  $028E22 |         ROM |      |            table | 
;    $0137 |    $2A |  $02A9E1 |   $04F8 |  $0204F8 |  RAM-mirror |      |            table | -> $7E04F8
;    $0138 |    $2C |  $02A9E3 |   $A9FA |  $02A9FA |         ROM |      |            table | 
;    $0139 |    $2E |  $02A9E5 |   $0006 |  $020006 |  RAM-mirror |      |            table | -> $7E0006
;    $013A |    $30 |  $02A9E7 |   $2248 |  $022248 |      RAM/IO |      |            table | -> I/O $2248
;    $013B |    $32 |  $02A9E9 |   $BF87 |  $02BF87 |         ROM |      |            table | 
;    $013C |    $34 |  $02A9EB |   $A903 |  $02A903 |         ROM |      |            table | 
;    $013D |    $36 |  $02A9ED |   $0115 |  $020115 |  RAM-mirror |      |            table | -> $7E0115
;    $013E |    $38 |  $02A9EF |   $229B |  $02229B |      RAM/IO |      |            table | -> I/O $229B
;    $013F |    $3A |  $02A9F1 |   $A377 |  $02A377 |         ROM |      |            table | 
;    $0140 |    $3C |  $02A9F3 |   $6803 |  $026803 | SRAM-mirror |      |            table | -> SRAM $0803
;    $0141 |    $3E |  $02A9F5 |   $425D |  $02425D |      RAM/IO |      |            table | -> I/O $425D
;    $0142 |    $40 |  $02A9F7 |   $9D70 |  $029D70 |         ROM |      |            table | 
;    $0143 |    $42 |  $02A9F9 |   $7042 |  $027042 | SRAM-mirror |      |            table | -> SRAM $1042
;    $0144 |    $44 |  $02A9FB |   $30A9 |  $0230A9 |      RAM/IO |      |            table | -> I/O $30A9
;    $0145 |    $46 |  $02A9FD |   $9D00 |  $029D00 |         ROM |      |            table | 
;    $0146 |    $48 |  $02A9FF |   $7A96 |  $027A96 | SRAM-mirror |      |            table | -> SRAM $1A96
;    $0147 |    $4A |  $02AA01 |   $989D |  $02989D |         ROM |      |            table | 
;    $0148 |    $4C |  $02AA03 |   $9D7A |  $029D7A |         ROM |      |            table | 
;    $0149 |    $4E |  $02AA05 |   $7AF6 |  $027AF6 | SRAM-mirror |      |            table | -> SRAM $1AF6
;    $014A |    $50 |  $02AA07 |   $D89D |  $02D89D |         ROM |      |            table | 
;    $014B |    $52 |  $02AA09 |   $A979 |  $02A979 |         ROM |      |            table | 
;    $014C |    $54 |  $02AA0B |   $FE80 |  $02FE80 |         ROM |      |            table | 
;    $014D |    $56 |  $02AA0D |   $229D |  $02229D |      RAM/IO |      |            table | -> I/O $229D
;    $014E |    $58 |  $02AA0F |   $A972 |  $02A972 |         ROM |      |            table | 
;    $014F |    $5A |  $02AA11 |   $0008 |  $020008 |  RAM-mirror |      |            table | -> $7E0008
;    $0150 |    $5C |  $02AA13 |   $429D |  $02429D |      RAM/IO |      |            table | -> I/O $429D
;    $0151 |    $5E |  $02AA15 |   $BD75 |  $02BD75 |         ROM |      |            table | 
;    $0152 |    $60 |  $02AA17 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0153 |    $62 |  $02AA19 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $0154 |    $64 |  $02AA1B |   $9DFF |  $029DFF |         ROM |      |            table | 
;    $0155 |    $66 |  $02AA1D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0156 |    $68 |  $02AA1F |   $BB60 |  $02BB60 |         ROM |      |            table | 
;    $0157 |    $6A |  $02AA21 |   $F422 |  $02F422 |         ROM |      |            table | 
;    $0158 |    $6C |  $02AA23 |   $02A4 |  $0202A4 |  RAM-mirror |      |            table | -> $7E02A4
;    $0159 |    $6E |  $02AA25 |   $00A9 |  $0200A9 |  RAM-mirror |      |            table | -> $7E00A9
;    $015A |    $70 |  $02AA27 |   $8000 |  $028000 |         ROM |      |            table | 
;    $015B |    $72 |  $02AA29 |   $BBBD |  $02BBBD |         ROM |      |            table | 
;    $015C |    $74 |  $02AA2B |   $8722 |  $028722 |         ROM |      |            table | 
;    $015D |    $76 |  $02AA2D |   $03BF |  $0203BF |  RAM-mirror |      |            table | -> $7E03BF
;    $015E |    $78 |  $02AA2F |   $00A9 |  $0200A9 |  RAM-mirror |      |            table | -> $7E00A9
;    $015F |    $7A |  $02AA31 |   $9DFB |  $029DFB |         ROM |      |            table | 
;    $0160 |    $7C |  $02AA33 |   $7222 |  $027222 | SRAM-mirror |      |            table | -> SRAM $1222
;    $0161 |    $7E |  $02AA35 |   $BB60 |  $02BB60 |         ROM |      |            table | 
;    $0162 |    $80 |  $02AA37 |   $82BD |  $0282BD |         ROM |      |            table | 
;    $0163 |    $82 |  $02AA39 |   $8571 |  $028571 |         ROM |      |            table | 
;    $0164 |    $84 |  $02AA3B |   $A900 |  $02A900 |         ROM |      |            table | 
;    $0165 |    $86 |  $02AA3D |   $0003 |  $020003 |  RAM-mirror |      |            table | -> $7E0003
;    $0166 |    $88 |  $02AA3F |   $0285 |  $020285 |  RAM-mirror |      |            table | -> $7E0285
;    $0167 |    $8A |  $02AA41 |   $15A9 |  $0215A9 |  RAM-mirror |      |            table | -> $7E15A9
;    $0168 |    $8C |  $02AA43 |   $2201 |  $022201 |      RAM/IO |      |            table | -> I/O $2201
;    $0169 |    $8E |  $02AA45 |   $A364 |  $02A364 |         ROM |      |            table | 
;    $016A |    $90 |  $02AA47 |   $9003 |  $029003 |         ROM |      |            table | 
;    $016B |    $92 |  $02AA49 |   $BDD7 |  $02BDD7 |         ROM |      |            table | 
;    $016C |    $94 |  $02AA4B |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $016D |    $96 |  $02AA4D |   $E299 |  $02E299 |         ROM |      |            table | 
;    $016E |    $98 |  $02AA4F |   $A570 |  $02A570 |         ROM |      |            table | 
;    $016F |    $9A |  $02AA51 |   $3800 |  $023800 |      RAM/IO |      |            table | -> I/O $3800
;    $0170 |    $9C |  $02AA53 |   $10E9 |  $0210E9 |  RAM-mirror |      |            table | -> $7E10E9
;    $0171 |    $9E |  $02AA55 |   $9900 |  $029900 |         ROM |      |            table | 
;    $0172 |    $A0 |  $02AA57 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
;    $0173 |    $A2 |  $02AA59 |   $0085 |  $020085 |  RAM-mirror |      |            table | -> $7E0085
;    $0174 |    $A4 |  $02AA5B |   $30A9 |  $0230A9 |      RAM/IO |      |            table | -> I/O $30A9
;    $0175 |    $A6 |  $02AA5D |   $9900 |  $029900 |         ROM |      |            table | 
;    $0176 |    $A8 |  $02AA5F |   $7A96 |  $027A96 | SRAM-mirror |      |            table | -> SRAM $1A96
;    $0177 |    $AA |  $02AA61 |   $9899 |  $029899 |         ROM |      |            table | 
;    $0178 |    $AC |  $02AA63 |   $997A |  $02997A |         ROM |      |            table | 
;    $0179 |    $AE |  $02AA65 |   $7AF6 |  $027AF6 | SRAM-mirror |      |            table | -> SRAM $1AF6
;    $017A |    $B0 |  $02AA67 |   $D899 |  $02D899 |         ROM |      |            table | 
;    $017B |    $B2 |  $02AA69 |   $A979 |  $02A979 |         ROM |      |            table | 
;    $017C |    $B4 |  $02AA6B |   $FE80 |  $02FE80 |         ROM |      |            table | 
;    $017D |    $B6 |  $02AA6D |   $2299 |  $022299 |      RAM/IO |      |            table | -> I/O $2299
;    $017E |    $B8 |  $02AA6F |   $A972 |  $02A972 |         ROM |      |            table | 
;    $017F |    $BA |  $02AA71 |   $0008 |  $020008 |  RAM-mirror |      |            table | -> $7E0008
;    $0180 |    $BC |  $02AA73 |   $4299 |  $024299 |      RAM/IO |      |            table | -> I/O $4299
;    $0181 |    $BE |  $02AA75 |   $B975 |  $02B975 |         ROM |      |            table | 
;    $0182 |    $C0 |  $02AA77 |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0183 |    $C2 |  $02AA79 |   $E029 |  $02E029 |         ROM |      |            table | 
;    $0184 |    $C4 |  $02AA7B |   $99FF |  $0299FF |         ROM |      |            table | 
;    $0185 |    $C6 |  $02AA7D |   $6FA2 |  $026FA2 | SRAM-mirror |      |            table | -> SRAM $0FA2
;    $0186 |    $C8 |  $02AA7F |   $02C6 |  $0202C6 |  RAM-mirror |      |            table | -> $7E02C6
;    $0187 |    $CA |  $02AA81 |   $BED0 |  $02BED0 |         ROM |      |            table | 
;    $0188 |    $CC |  $02AA83 |   $214C |  $02214C |      RAM/IO |      |            table | -> I/O $214C
;    $0189 |    $CE |  $02AA85 |   $BBAA |  $02BBAA |         ROM | direct RTS |            table | 
;    $018A |    $D0 |  $02AA87 |   $DEAD |  $02DEAD |         ROM |      |            table | 
;    $018B |    $D2 |  $02AA89 |   $D060 |  $02D060 |         ROM |      |            table | 
;    $018C |    $D4 |  $02AA8B |   $A97D |  $02A97D |         ROM |      |            table | 
;    $018D |    $D6 |  $02AA8D |   $0002 |  $020002 |  RAM-mirror |      |            table | -> $7E0002
;    $018E |    $D8 |  $02AA8F |   $AC8D |  $02AC8D |         ROM |      |            table | 
;    $018F |    $DA |  $02AA91 |   $9C60 |  $029C60 |         ROM |      |            table | 
;    $0190 |    $DC |  $02AA93 |   $617A |  $02617A | SRAM-mirror |      |            table | -> SRAM $017A
;    $0191 |    $DE |  $02AA95 |   $7C9C |  $027C9C | SRAM-mirror |      |            table | -> SRAM $1C9C
;    $0192 |    $E0 |  $02AA97 |   $F661 |  $02F661 |         ROM |      |            table | 
;    $0193 |    $E2 |  $02AA99 |   $A918 |  $02A918 |         ROM |      |            table | 
;    $0194 |    $E4 |  $02AA9B |   $0054 |  $020054 |  RAM-mirror |      |            table | -> $7E0054
;    $0195 |    $E6 |  $02AA9D |   $969D |  $02969D |         ROM |      |            table | 
;    $0196 |    $E8 |  $02AA9F |   $A07A |  $02A07A |         ROM |      |            table | 
;    $0197 |    $EA |  $02AAA1 |   $A904 |  $02A904 |         ROM |      |            table | 
;    $0198 |    $EC |  $02AAA3 |   $008C |  $02008C |  RAM-mirror |      |            table | -> $7E008C
;    $0199 |    $EE |  $02AAA5 |   $4E22 |  $024E22 |      RAM/IO |      |            table | -> I/O $4E22
;    $019A |    $F0 |  $02AAA7 |   $03A3 |  $0203A3 |  RAM-mirror |      |            table | -> $7E03A3
;    $019B |    $F2 |  $02AAA9 |   $1A98 |  $021A98 |  RAM-mirror |      |            table | -> $7E1A98
;    $019C |    $F4 |  $02AAAB |   $369D |  $02369D |      RAM/IO |      |            table | -> I/O $369D
;    $019D |    $F6 |  $02AAAD |   $AD7A |  $02AD7A |         ROM |      |            table | 
;    $019E |    $F8 |  $02AAAF |   $608C |  $02608C | SRAM-mirror |      |            table | -> SRAM $008C
;    $019F |    $FA |  $02AAB1 |   $E299 |  $02E299 |         ROM |      |            table | 
;    $01A0 |    $FC |  $02AAB3 |   $AD70 |  $02AD70 |         ROM |      |            table | 
;    $01A1 |    $FE |  $02AAB5 |   $6090 |  $026090 | SRAM-mirror |      |            table | -> SRAM $0090
;    $01A2 |    $00 |  $02A9B7 |   $A9CB |  $02A9CB |         ROM | valid table |      intentional | 
;    $01A3 |    $02 |  $02A9B9 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $01A4 |    $04 |  $02A9BB |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $01A5 |    $06 |  $02A9BD |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $01A6 |    $08 |  $02A9BF |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $01A7 |    $0A |  $02A9C1 |   $AA20 |  $02AA20 |         ROM | valid table |      intentional | 
;    $01A8 |    $0C |  $02A9C3 |   $AA2A |  $02AA2A |         ROM | valid table |      intentional | 
;    $01A9 |    $0E |  $02A9C5 |   $A981 |  $02A981 |         ROM | valid table, direct RTS |      intentional | 
;    $01AA |    $10 |  $02A9C7 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $01AB |    $12 |  $02A9C9 |   $AA36 |  $02AA36 |         ROM | valid table |      intentional | 
;    $01AC |    $14 |  $02A9CB |   $BDBB |  $02BDBB |         ROM |      |            table | 
;    $01AD |    $16 |  $02A9CD |   $70E2 |  $0270E2 | SRAM-mirror |      |            table | -> SRAM $10E2
;    $01AE |    $18 |  $02A9CF |   $008D |  $02008D |  RAM-mirror |      |            table | -> $7E008D
;    $01AF |    $1A |  $02A9D1 |   $BD00 |  $02BD00 |         ROM | direct RTS |            table | 
;    $01B0 |    $1C |  $02A9D3 |   $7182 |  $027182 | SRAM-mirror |      |            table | -> SRAM $1182
