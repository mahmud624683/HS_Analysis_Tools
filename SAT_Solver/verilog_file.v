INPUT(G1gat)
INPUT(G4gat)
INPUT(G8gat)
INPUT(G11gat)
INPUT(G14gat)
INPUT(G17gat)
INPUT(G21gat)
INPUT(G24gat)
INPUT(G27gat)
INPUT(G30gat)
INPUT(G34gat)
INPUT(G37gat)
INPUT(G40gat)
INPUT(G43gat)
INPUT(G47gat)
INPUT(G50gat)
INPUT(G53gat)
INPUT(G56gat)
INPUT(G60gat)
INPUT(G63gat)
INPUT(G66gat)
INPUT(G69gat)
INPUT(G73gat)
INPUT(G76gat)
INPUT(G79gat)
INPUT(G82gat)
INPUT(G86gat)
INPUT(G89gat)
INPUT(G92gat)
INPUT(G95gat)
INPUT(G99gat)
INPUT(G102gat)
INPUT(G105gat)
INPUT(G108gat)
INPUT(G112gat)
INPUT(G115gat)
OUTPUT(G223gat)
OUTPUT(G329gat)
OUTPUT(G370gat)
OUTPUT(G421gat)
OUTPUT(G430gat)
OUTPUT(G431gat)
OUTPUT(G432gat)

G118gat = not(G1gat)
G119gat = not(G4gat)
G122gat = not(G11gat)
G123gat = not(G17gat)
G126gat = not(G24gat) 
G127gat = not(G30gat)
G130gat = not(G37gat)   
G131gat = not(G43gat)
G134gat = not(G50gat)
G135gat = not(G56gat)
G138gat = not(G63gat)
G139gat = not(G69gat)
G142gat = not(G76gat)
G143gat = not(G82gat)
G146gat = not(G89gat)
G147gat = not(G95gat)
G150gat = not(G102gat)
G151gat = not(G108gat)
G154gat = nand(not(G1gat), G4gat)
G157gat = nor(G8gat, G119gat)
G158gat = nor(G14gat, G119gat)
G159gat = nand(G122gat, G17gat)
G162gat = nand(G126gat, G30gat)
G165gat = nand(G130gat, G43gat)
G168gat = nand(G134gat, G56gat)
G171gat = nand(G138gat, G69gat)
G174gat = nand(G142gat, G82gat)
G177gat = nand(G146gat, G95gat)
G180gat = nand(G150gat, G108gat)
G183gat = nor(G21gat, G123gat)
G184gat = nor(G27gat, G123gat)
G185gat = nor(G34gat, G127gat)
G186gat = nor(G40gat, G127gat)
G187gat = nor(G47gat, G131gat)
G188gat = nor(G53gat, G131gat)
G189gat = nor(G60gat, G135gat)
G190gat = nor(G66gat, G135gat)
G191gat = nor(G73gat, G139gat)
G192gat = nor(G79gat, G139gat)
G193gat = nor(G86gat, G143gat)
G194gat = nor(G92gat, G143gat)
G195gat = nor(G99gat, G147gat)
G196gat = nor(G105gat, G147gat)
G197gat = nor(G112gat, G151gat)
G198gat = nor(G115gat, G151gat)
G199gat = and(G154gat, G159gat, G162gat, G165gat, G168gat, G171gat, G174gat, G177gat, G180gat)
G203gat = not(G199gat)
G213gat = not(G199gat)
G223gat = not(G199gat)


G224gat = xor(G203gat, G154gat)
G227gat = xor(G203gat, G159gat)
G230gat = xor(G203gat, G162gat)
G233gat = xor(G203gat, G165gat)
G236gat = xor(G203gat, G168gat)
G239gat = xor(G203gat, G171gat)
G242gat = nand(G1gat, G213gat)
G243gat = xor(G203gat, G174gat)
G246gat = nand(G213gat, G11gat)
G247gat = xor(G203gat, G177gat)
G250gat = nand(G213gat, G24gat)
G251gat = xor(G203gat, G180gat)
G254gat = nand(G213gat, G37gat)
G255gat = nand(G213gat, G50gat)
G256gat = nand(G213gat, G63gat)
G257gat = nand(G213gat, G76gat)
G258gat = nand(G213gat, G89gat)
G259gat = nand(G213gat, G102gat)
G260gat = nand(G224gat, G157gat)
G263gat = nand(G224gat, G158gat)
G264gat = nand(G227gat, G183gat)
G267gat = nand(G230gat, G185gat)
G270gat = nand(G233gat, G187gat)
G273gat = nand(G236gat, G189gat)
G276gat = nand(G239gat, G191gat)
G279gat = nand(G243gat, G193gat)
G282gat = nand(G247gat, G195gat)
G285gat = nand(G251gat, G197gat)
G288gat = nand(G227gat, G184gat)
G289gat = nand(G230gat, G186gat)
G290gat = nand(G233gat, G188gat)
G291gat = nand(G236gat, G190gat)
G292gat = nand(G239gat, G192gat)
G293gat = nand(G243gat, G194gat)
G294gat = nand(G247gat, G196gat)
G295gat = nand(G251gat, G198gat)
G296gat = and(G260gat, G264gat, G267gat, G270gat, G273gat, G276gat, G279gat, G282gat, G285gat)
G300gat = not(G263gat)
G301gat = not(G288gat)
G302gat = not(G289gat)
G303gat = not(G290gat)
G304gat = not(G291gat)
G305gat = not(G292gat)
G306gat = not(G293gat)
G307gat = not(G294gat)
G308gat = not(G295gat)
G309gat = not(G296gat)
G319gat = not(G296gat)
G329gat = not(G296gat)
G330gat = xor(G309gat, G260gat)
G331gat = xor(G309gat, G264gat)
G332gat = xor(G309gat, G267gat)
G333gat = xor(G309gat, G270gat)
G334gat = nand(G8gat, G319gat)
G335gat = xor(G309gat, G273gat)
G336gat = nand(G319gat, G21gat)
G337gat = xor(G309gat, G276gat)
G338gat = nand(G319gat, G34gat)
G339gat = xor(G309gat, G279gat)
G340gat = nand(G319gat, G47gat)
G341gat = xor(G309gat, G282gat)
G342gat = nand(G319gat, G60gat)
G343gat = xor(G309gat, G285gat)
G344gat = nand(G319gat, G73gat)
G345gat = nand(G319gat, G86gat)
G346gat = nand(G319gat, G99gat)
G347gat = nand(G319gat, G112gat)
G348gat = nand(G330gat, G300gat)
G349gat = nand(G331gat, G301gat)
G350gat = nand(G332gat, G302gat)
G351gat = nand(G333gat, G303gat)
G352gat = nand(G335gat, G304gat)
G353gat = nand(G337gat, G305gat)
G354gat = nand(G339gat, G306gat)
G355gat = nand(G341gat, G307gat)
G356gat = nand(G343gat, G308gat)
G357gat = and(G348gat, G349gat, G350gat, G351gat, G352gat, G353gat, G354gat, G355gat, G356gat)
G360gat = not(G357gat)
G370gat = not(G357gat)
G371gat = nand(G14gat, G360gat)
G372gat = nand(G360gat, G27gat)
G373gat = nand(G360gat, G40gat)
G374gat = nand(G360gat, G53gat)
G375gat = nand(G360gat, G66gat)
G376gat = nand(G360gat, G79gat)
G377gat = nand(G360gat, G92gat)
G378gat = nand(G360gat, G105gat)
G379gat = nand(G360gat, G115gat)
G380gat = nand(G4gat, G242gat, G334gat, G371gat)
G381gat = nand(G246gat, G336gat, G372gat, G17gat)
G386gat = nand(G250gat, G338gat, G373gat, G30gat)
G393gat = nand(G254gat, G340gat, G374gat, G43gat)
G399gat = nand(G255gat, G342gat, G375gat, G56gat)
G404gat = nand(G256gat, G344gat, G376gat, G69gat)
G407gat = nand(G257gat, G345gat, G377gat, G82gat)
G411gat = nand(G258gat, G346gat, G378gat, G95gat)
G414gat = nand(G259gat, G347gat, G379gat, G108gat)
G415gat = not(G380gat)
G416gat = and(G381gat, G386gat, G393gat, G399gat, G404gat, G407gat, G411gat, G414gat)
G417gat = not(G393gat)
G418gat = not(G404gat)
G419gat = not(G407gat)
G420gat = not(G411gat)
G421gat = nor(G415gat, G416gat)
G422gat = nand(G386gat, G417gat)
G425gat = nand(G386gat, G393gat, G418gat, G399gat)
G428gat = nand(G399gat, G393gat, G419gat)
G429gat = nand(G386gat, G393gat, G407gat, G420gat)
G430gat = nand(G381gat, G386gat, G422gat, G399gat)
G431gat = nand(G381gat, G386gat, G425gat, G428gat)
G432gat = nand(G381gat, G422gat, G425gat, G429gat)