### Data Collecting

We collect enzyme, cofactor, kinetic info from open-access databases. In order to facilitate use and query, we extract the desired info and rebuild our own database, and integrate it into our web software.

### Databases Building

We mainly maintain 3 kinds of databases: reaction DBs, enzyme DBs and kinetic info DBs. Reaction DBs contain information of reactions, mostly used to in prescreening process, to improve MEI's performance. Enzyme DBs include the basic info of each enzyme number, such as organisms, enzyme name and so on. Kinetic info DBs have precise pH, Km, Kcat and temperature info of each enzyme. We obtain these data from open-access databases, such as Brenda and ExplorEnz. A lot of optimization has been done when buliding our self-construct database. In our database, we store the reactions and moledules in SMILES format, instead of the name or chemical formula in the source database. This is to expand the representation power of text info. In support of fuzzy search, we introduce SOUNDEX algorithm, and save an extra soundex column for each column representing a name, so that MEI is robust of the case when user has a typo in the query. 
