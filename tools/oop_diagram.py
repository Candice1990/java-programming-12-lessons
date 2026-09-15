"""Code-native, scalable teaching diagram for the four OOP principles."""

def diagram():
    return '''<figure class="visual-card" style="margin:24px 0"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 960 870" role="img" aria-labelledby="oop-map-title oop-map-desc" style="display:block;width:100%;height:auto">
<title id="oop-map-title">OOP: four important concepts</title>
<desc id="oop-map-desc">OOP branches into abstraction, encapsulation, inheritance and polymorphism. Television illustrations show simple controls, protected internal state, specialized television types, and different responses to the same operation.</desc>
<defs><g id="oop-tv" fill="none" stroke="currentColor" stroke-width="3" stroke-linejoin="round"><rect width="100" height="65" rx="7"/><rect x="9" y="9" width="68" height="45" rx="3"/><circle cx="88" cy="25" r="4"/><path d="M84 40h8M30 65l-7 9M70 65l7 9"/></g></defs>
<rect width="960" height="870" fill="#faf7ef"/>
<g font-family="Arial, sans-serif" fill="#18282c">
<rect x="280" y="25" width="400" height="80" rx="12" fill="#182c31"/>
<text x="480" y="59" text-anchor="middle" font-size="25" font-weight="700" fill="#fff">Object-Oriented Programming</text>
<text x="480" y="87" text-anchor="middle" font-size="17" fill="#c9ddd5">Four important concepts</text>
<g fill="none" stroke="#a95736" stroke-width="2"><path d="M480 105v25H25v480h15M480 130h455v480h-15M25 225h15M935 225h-15"/></g>
<rect x="40" y="155" width="425" height="320" rx="12" fill="#edf1e9" stroke="#b7c5b7"/>
<rect x="495" y="155" width="425" height="320" rx="12" fill="#f1e7d8" stroke="#cbb99f"/>
<rect x="40" y="510" width="425" height="325" rx="12" fill="#f1e7d8" stroke="#cbb99f"/>
<rect x="495" y="510" width="425" height="325" rx="12" fill="#edf1e9" stroke="#b7c5b7"/>
<text x="65" y="194" font-size="24" font-weight="700">01  Abstraction</text>
<text x="65" y="224" font-size="18">Expose useful operations.</text>
<use href="#oop-tv" x="240" y="260" color="#355e52"/>
<rect x="96" y="256" width="46" height="91" rx="8" fill="#faf7ef" stroke="#355e52" stroke-width="2"/>
<circle cx="119" cy="279" r="7" fill="#a95736"/><path d="M111 310h16M119 302v16" fill="none" stroke="#355e52" stroke-width="2"/>
<path d="M158 294h62l-8-6m8 6-8 6" fill="none" stroke="#a95736" stroke-width="2"/>
<text x="65" y="384" font-size="19" font-weight="700">Press Power → the TV turns on.</text>
<text x="65" y="416" font-size="17">You use the controls without knowing</text><text x="65" y="441" font-size="17">how the circuits work.</text>
<text x="520" y="194" font-size="24" font-weight="700">02  Encapsulation</text>
<text x="520" y="224" font-size="18">Keep state and behavior together.</text>
<rect x="548" y="249" width="317" height="108" rx="10" fill="#faf7ef" stroke="#355e52" stroke-width="2"/>
<text x="707" y="278" text-anchor="middle" font-size="17">TV object</text><text x="707" y="307" text-anchor="middle" font-size="18" font-weight="700">private volume</text><text x="707" y="337" text-anchor="middle" font-size="17">setVolume checks 0–100</text>
<text x="520" y="384" font-size="19" font-weight="700">Change volume through a method.</text><text x="520" y="416" font-size="17">The object controls access to its state</text><text x="520" y="441" font-size="17">and rejects an invalid setting.</text>
<text x="65" y="550" font-size="24" font-weight="700">03  Inheritance</text><text x="65" y="580" font-size="18">Build a specialized kind of a class.</text>
<rect x="180" y="603" width="140" height="38" rx="6" fill="#faf7ef" stroke="#355e52"/><text x="250" y="629" text-anchor="middle" font-size="19">Television</text>
<path d="M250 641v20H145v18M250 661h105v18" stroke="#355e52" stroke-width="2" fill="none"/>
<text x="145" y="705" text-anchor="middle" font-size="19" font-weight="700">SmartTV</text><text x="355" y="705" text-anchor="middle" font-size="19" font-weight="700">BasicTV</text>
<text x="65" y="757" font-size="19" font-weight="700">A SmartTV is a Television.</text><text x="65" y="789" font-size="17">It inherits behavior and can add features.</text>
<text x="520" y="550" font-size="24" font-weight="700">04  Polymorphism</text><text x="520" y="580" font-size="18">Same operation, different behavior.</text>
<text x="707" y="621" text-anchor="middle" font-size="20" font-weight="700">turnOn()</text><path d="M707 632v18H615v20M707 650h100v20" stroke="#355e52" stroke-width="2" fill="none"/>
<text x="615" y="693" text-anchor="middle" font-size="18" font-weight="700">SmartTV</text><text x="807" y="693" text-anchor="middle" font-size="18" font-weight="700">BasicTV</text><text x="615" y="720" text-anchor="middle" font-size="16">Shows apps</text><text x="807" y="720" text-anchor="middle" font-size="16">Shows a channel</text>
<text x="520" y="757" font-size="19" font-weight="700">Each type supplies its own behavior.</text><text x="520" y="789" font-size="17">The actual object determines what runs.</text>
</g></svg></figure>'''
