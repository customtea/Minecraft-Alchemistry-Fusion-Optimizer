from collections import OrderedDict
import typing as tp

class Element():
    def __init__(self, number: int, name: str, acronym: str) -> None:
        self.__id = number
        self.num = number
        self.name = name
        self.acronym = acronym

    def __int__(self) -> int:
        return self.num
    
    def __str__(self) -> str:
        return f"{self.num}:{self.name}"

    def __eq__(self, other: object) -> bool:
        if isinstance(other, self.__class__):
            return self.num == other.num
        else:
            another_class = other.__class__.__name__
            raise NotImplementedError(f'comparison between Element class and {another_class} is not supported')
    
    
    def __lt__(self, other) -> bool:
        if not isinstance(other, self.__class__):
            another_class = other.__class__.__name__
            raise NotImplementedError(f'comparison between Element class and {another_class} is not supported')
        return self.num < other.num

    def __hash__(self) -> int:
        return hash(self.__id)


class Elementum():
    table = OrderedDict()
    
    def __init__(self) -> None:
        pass

    def get4num(self, num: int) -> Element:
        return list(self.table.values())[num]

    def get4acro(self, acronym: str) -> Element:
        return self.table.get(acronym)


## Regist
Elementum.table["DUMMY"]    = Element(0,"DUMMY", "DUMMY")
Elementum.table["H"]        = Element(1,"Hydrogen","H")
Elementum.table["He"]       = Element(2,"Helium","He")
Elementum.table["Li"]       = Element(3,"Lithium","Li")
Elementum.table["Be"]       = Element(4,"Beryllium","Be")
Elementum.table["B"]        = Element(5,"Boron","B")
Elementum.table["C"]        = Element(6,"Carbon","C")
Elementum.table["N"]        = Element(7,"Nitrogen","N")
Elementum.table["O"]        = Element(8,"Oxygen","O")
Elementum.table["F"]        = Element(9,"Fluorine","F")
Elementum.table["Ne"]       = Element(10,"Neon","Ne")
Elementum.table["Na"]       = Element(11,"Sodium","Na")
Elementum.table["Mg"]       = Element(12,"Magnesium","Mg")
Elementum.table["Al"]       = Element(13,"Aluminium","Al")
Elementum.table["Si"]       = Element(14,"Silicon","Si")
Elementum.table["P"]        = Element(15,"Phosphorus","P")
Elementum.table["S"]        = Element(16,"Sulfur","S")
Elementum.table["Cl"]       = Element(17,"Chlorine","Cl")
Elementum.table["Ar"]       = Element(18,"Argon","Ar")
Elementum.table["K"]        = Element(19,"Potassium","K")
Elementum.table["Ca"]       = Element(20,"Calcium","Ca")
Elementum.table["Sc"]       = Element(21,"Scandium","Sc")
Elementum.table["Ti"]       = Element(22,"Titanium","Ti")
Elementum.table["V"]        = Element(23,"Vanadium","V")
Elementum.table["Cr"]       = Element(24,"Chromium","Cr")
Elementum.table["Mn"]       = Element(25,"Manganese","Mn")
Elementum.table["Fe"]       = Element(26,"Iron","Fe")
Elementum.table["Co"]       = Element(27,"Cobalt","Co")
Elementum.table["Ni"]       = Element(28,"Nickel","Ni")
Elementum.table["Cu"]       = Element(29,"Copper","Cu")
Elementum.table["Zn"]       = Element(30,"Zinc","Zn")
Elementum.table["Ga"]       = Element(31,"Gallium","Ga")
Elementum.table["Ge"]       = Element(32,"Germanium","Ge")
Elementum.table["As"]       = Element(33,"Arsenic","As")
Elementum.table["Se"]       = Element(34,"Selenium","Se")
Elementum.table["Br"]       = Element(35,"Bromine","Br")
Elementum.table["Kr"]       = Element(36,"Krypton","Kr")
Elementum.table["Rb"]       = Element(37,"Rubidium","Rb")
Elementum.table["Sr"]       = Element(38,"Strontium","Sr")
Elementum.table["Y"]        = Element(39,"Yttrium","Y")
Elementum.table["Zr"]       = Element(40,"Zirconium","Zr")
Elementum.table["Nb"]       = Element(41,"Niobium","Nb")
Elementum.table["Mo"]       = Element(42,"Molybdenum","Mo")
Elementum.table["Tc"]       = Element(43,"Technetium","Tc")
Elementum.table["Ru"]       = Element(44,"Ruthenium","Ru")
Elementum.table["Rh"]       = Element(45,"Rhodium","Rh")
Elementum.table["Pd"]       = Element(46,"Palladium","Pd")
Elementum.table["Ag"]       = Element(47,"Silver","Ag")
Elementum.table["Cd"]       = Element(48,"Cadmium","Cd")
Elementum.table["In"]       = Element(49,"Indium","In")
Elementum.table["Sn"]       = Element(50,"Tin","Sn")
Elementum.table["Sb"]       = Element(51,"Antimony","Sb")
Elementum.table["Te"]       = Element(52,"Tellurium","Te")
Elementum.table["I"]        = Element(53,"Iodine","I")
Elementum.table["Xe"]       = Element(54,"Xenon","Xe")
Elementum.table["Cs"]       = Element(55,"Caesium","Cs")
Elementum.table["Ba"]       = Element(56,"Barium","Ba")
Elementum.table["La"]       = Element(57,"Lanthanum","La")
Elementum.table["Ce"]       = Element(58,"Cerium","Ce")
Elementum.table["Pr"]       = Element(59,"Praseodymium","Pr")
Elementum.table["Nd"]       = Element(60,"Neodymium","Nd")
Elementum.table["Pm"]       = Element(61,"Promethium","Pm")
Elementum.table["Sm"]       = Element(62,"Samarium","Sm")
Elementum.table["Eu"]       = Element(63,"Europium","Eu")
Elementum.table["Gd"]       = Element(64,"Gadolinium","Gd")
Elementum.table["Tb"]       = Element(65,"Terbium","Tb")
Elementum.table["Dy"]       = Element(66,"Dysprosium","Dy")
Elementum.table["Ho"]       = Element(67,"Holmium","Ho")
Elementum.table["Er"]       = Element(68,"Erbium","Er")
Elementum.table["Tm"]       = Element(69,"Thulium","Tm")
Elementum.table["Yb"]       = Element(70,"Ytterbium","Yb")
Elementum.table["Lu"]       = Element(71,"Lutetium","Lu")
Elementum.table["Hf"]       = Element(72,"Hafnium","Hf")
Elementum.table["Ta"]       = Element(73,"Tantalum","Ta")
Elementum.table["W"]        = Element(74,"Tungsten","W")
Elementum.table["Re"]       = Element(75,"Rhenium","Re")
Elementum.table["Os"]       = Element(76,"Osmium","Os")
Elementum.table["Ir"]       = Element(77,"Iridium","Ir")
Elementum.table["Pt"]       = Element(78,"Platinum","Pt")
Elementum.table["Au"]       = Element(79,"Gold","Au")
Elementum.table["Hg"]       = Element(80,"Mercury","Hg")
Elementum.table["Tl"]       = Element(81,"Thallium","Tl")
Elementum.table["Pb"]       = Element(82,"Lead","Pb")
Elementum.table["Bi"]       = Element(83,"Bismuth","Bi")
Elementum.table["Po"]       = Element(84,"Polonium","Po")
Elementum.table["At"]       = Element(85,"Astatine","At")
Elementum.table["Rn"]       = Element(86,"Radon","Rn")
Elementum.table["Fr"]       = Element(87,"Francium","Fr")
Elementum.table["Ra"]       = Element(88,"Radium","Ra")
Elementum.table["Ac"]       = Element(89,"Actinium","Ac")
Elementum.table["Th"]       = Element(90,"Thorium","Th")
Elementum.table["Pa"]       = Element(91,"Protactinium","Pa")
Elementum.table["U"]        = Element(92,"Uranium","U")
Elementum.table["Np"]       = Element(93,"Neptunium","Np")
Elementum.table["Pu"]       = Element(94,"Plutonium","Pu")
Elementum.table["Am"]       = Element(95,"Americium","Am")
Elementum.table["Cm"]       = Element(96,"Curium","Cm")
Elementum.table["Bk"]       = Element(97,"Berkelium","Bk")
Elementum.table["Cf"]       = Element(98,"Californium","Cf")
Elementum.table["Es"]       = Element(99,"Einsteinium","Es")
Elementum.table["Fm"]       = Element(100,"Fermium","Fm")
Elementum.table["Md"]       = Element(101,"Mendelevium","Md")
Elementum.table["No"]       = Element(102,"Nobelium","No")
Elementum.table["Lr"]       = Element(103,"Lawrencium","Lr")
Elementum.table["Rf"]       = Element(104,"Rutherfordium","Rf")
Elementum.table["Db"]       = Element(105,"Dubnium","Db")
Elementum.table["Sg"]       = Element(106,"Seaborgium","Sg")
Elementum.table["Bh"]       = Element(107,"Bohrium","Bh")
Elementum.table["Hs"]       = Element(108,"Hassium","Hs")
Elementum.table["Mt"]       = Element(109,"Meitnerium","Mt")
Elementum.table["Ds"]       = Element(110,"Darmstadtium","Ds")
Elementum.table["Rg"]       = Element(111,"Roentgenium","Rg")
Elementum.table["Cn"]       = Element(112,"Copernicium","Cn")
Elementum.table["Nh"]       = Element(113,"Nihonium","Nh")
Elementum.table["Fl"]       = Element(114,"Flerovium","Fl")
Elementum.table["Mc"]       = Element(115,"Moscovium","Mc")
Elementum.table["Lv"]       = Element(116,"Livermorium","Lv")
Elementum.table["Ts"]       = Element(117,"Tennessine","Ts")
Elementum.table["Og"]       = Element(118,"Oganesson","Og")
