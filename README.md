# CORDIS-DB-EU-Projects-Scraper

This project aims to download information about European Funded Projects from the [CORDIS DB](http://cordis.europa.eu/home_en.html).

### Goals

* Conduct statistical analyses
* Data-Journalism
* Create an 'almost' ready-to-use DB

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.
### Prerequisites

First clone ```git clone https://github.com/poltys/CORDIS-DB-EU-Projects-Scraper.git```

You will have to install Scrapy (and needed dependencies) in order to use it.

You can run ```sh install-dependencies.sh``` or ```pip install --user Scrapy```

### How to use

Run ```scrapy crawl cordis -o "filename"."extension"```.

* If you want to download information about a specific project you will have to change the following ```start_urls = ['http://cordis.europa.eu/project/rcn/%d_en.html' %(n) for n in range(210216, 210217)]``` in ```spiders/cordis_spider.py```.

* You can also extract from specific urls (sample urls.txt H2020 EU1)
* ```name = 'cordis'
  f = open("urls.txt")
  start_urls = [url.strip() for url in f.readlines()]
  f.close()```

* You can decide to scrape which information extract by modifying the keywords ```if response.xpath('//*[@id="ica:content"][contains(.,"water") and contains(.,"drinking water")]'):```

### Data Sample [STOP-IT H2020 Project](http://cordis.europa.eu/project/rcn/210216_en.html)

Scrapy gives you the opportunity to download your data in different formats: csv, jl, json, xml.
```
[{
  "Partners": ["STIFTELSEN SINTEF", "IWW RHEINISCH WESTFALISCHES INSTITUT FUR WASSERFORSCHUNG GEMEINNUTZIGE GMBH", "CETAQUA, CENTRO TECNOLOGICO DEL AGUA, FUNDACION PRIVADA", "KWR WATER B.V.", "FUNDACIO EURECAT", "TECHNION - ISRAEL INSTITUTE OF TECHNOLOGY", "ATOS SPAIN SA", "MEKOROT WATER COMPANY LIMITED", "AIGUES DE BARCELONA, EMPRESA METROPOLITANA DE GESTIO DEL CICLE INTEGRAL DE L'AIGUA SA", "HESSENWASSER GMBH & CO. KG", "OSLO KOMMUNE", "INSTITUTE OF COMMUNICATION AND COMPUTER SYSTEMS", "BERGEN KOMMUNE", "BERLINER WASSERBETRIEBE", "EUROPEAN WATER SUPPLY AND SANITATION TECHNOLOGY PLATFORM", "PNO INNOVATION", "BEIT TOCHNA APLICATZIA LTD", "EMPRESA MUNICIPAL DE ABASTECIMIENTO Y SANEAMIENTO DE GRANADA SA", "WORLDSENSING SL", "RISA SICHERHEITSANALYSEN GMBH", "MNEMONIC AS", "VLAAMSE MAATSCHAPPIJ VOORWATERVOORZIENING CVBA"],
  "EU_Contribution": ["EUR 8 255 319,50"],
  "Project_Title": ["Strategic, Tactical, Operational Protection of water Infrastructure against cyber-physical Threats"],
  "Total_Cost": ["EUR 9 616 525,18"],
  "Country": ["Norway", "Germany", "Spain", "Netherlands", "Spain", "Israel", "Spain", "Israel", "Spain", "Germany", "Norway", "Greece", "Norway", "Germany", "Belgium", "Belgium", "Israel", "Spain", "Spain", "Germany", "Norway", "Belgium"],
  "Project_ACR": ["STOP-IT"],
  "Technology_Description": "Water critical infrastructures (CIs) are essential for human society, life and health and they can be endangered by physical/cyber threats with severe societal consequences. To address this, STOP-IT assembles a team of major Water Utilities, industrial technology developers, high tech SMEs and top EU R&D providers. It organizes communities of practice for water systems protection to identify current and future risk landscapes and to co-develop an all-hazards risk management framework for the physical and cyber protection of water CIs. Prevention, Detection, Response and Mitigation of relevant risks at strategic, tactical and operational levels of planning will be taken into account to generate modular solutions (technologies, tools and guidelines) and an integrated software platform. STOP-IT solutions are based on: a) mature technologies improved via their combination and embedment (incl. public warning systems, smart locks) and b) novel technologies whose TRL will be increased (incl. cyber threat incident services, secure wireless sensor communications modules, context-aware anomaly detection technologies; fault-tolerant control strategies for SCADA integrated sensors, high-volume real-time sensor data protection via blockchain schemes; authorization engines; irregular human detection using new computer vision methods and WiFi and efficient water contamination detection algorithms). STOP-IT solutions are demonstrated through a front-runner/follower approach where 4 advanced utilities, Aig\u00fces de Barcelona (ES), Berliner Wasserbetriebe (DE), MEKOROT (IL) and Oslo VAV (NO) are twinned with 4 less advanced, but ambitious ones, to stimulate mutual learning, transfer and uptake. Building on this solid basis STOP-IT delivers high impact through the creation of hands-on training, best practice guidelines, support for certification and standardization as well as by fostering market opportunities, also leveraging the EU water technology platform's multi-stakeholder network.",
  "To": ["2021-05-31, ongoing project"],
  "Meta": ["<meta name=\"WT.cg_s\" content=\"H2020-EU.3.7.4., H2020-EU.3.7.2.\">"],
  "Topic_s": ["CIP-01-2016-2017 - Prevention, detection, response and mitigation of the combination of physical and cyber threats to the critical infrastructure of Europe."],
  "Funding_scheme": ["IA - Innovation action"],
  "Coordinated_in": ["Norway"],
  "Activity": ["Research Organisations", "Research Organisations", "Research Organisations", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Research Organisations", "Higher or Secondary Education Establishments", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Public bodies (excluding Research Organisations and Secondary or Higher Education Establishments)", "Research Organisations", "Public bodies (excluding Research Organisations and Secondary or Higher Education Establishments)", "Public bodies (excluding Research Organisations and Secondary or Higher Education Establishments)", "Other", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)", "Private for-profit entities (excluding Higher or Secondary Education Establishments)"],
  "From": ["2017-06-01"],
  "Project_ID": ["740610"],
  "Call_for_Proposal": ["CIP-2016-2017-1"]
}]
```

## TODO

* Update ```install-dependencies.sh```
* Clean ```cordis_spider.py```
* Add Cron jobs
* Add pipelines

## Author

* **Simon Hardy** - *Initial work* - [poltys](https://github.com/poltys)

## License

This project is licensed under the MIT [License](LICENSE)
