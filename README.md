# LaserRomae - ETHRome24

## Installation and execution
If you have python installed, you can use a virtual environment to run the example:
```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
fastapi dev main.py
```

If you instead have docker installed and you prefer running the example in a container:
```bash
docker build -t laser-hackathon-example .
docker run -it --rm --name laser-hackathon-example -p 8000:8000 laser-hackathon-example
```

Whichever option you choose, after completing the associated steps you should have the application listening on port 8000.
Documentation is available at `http://localhost:8000/docs`

## Challenge requirements
- the solution does not need to be written in Python
- the code provided is for example only. The only process that needs to be preserved is the issuance of a credential to the whistleblower, upon receipt of a tip.  
  this credential must allow the whistleblower, and only the whistleblower, to access the tip at a later time.  
- In the full application, the whistleblower uses the key received to start a cookie session that allows him to perform some actions on the tip (e.g. adding its identity if not present, participating in an asynchronous chat with the employees that will manage the tip).  
Something similar needs to be possible in a valid submission (it's not necessary to implement it, it just needs to be possible).
- it's important not to affect the anonimity of the whistleblower. Given an anonymous tip:
    - it must not be possible to trace its creator
    - it must not be possible to identify other tips submitted by the same user
- you must not use external services that publicly track information that, when cross-referenced with tip metadata (e.g. creation date), allow the person making the report to be identified

[Here](https://builders-garden.notion.site/Prizes-and-Bounties-67cc396a9bef4d7ab478d04c124dc4df#10c679ed099e806d9ecae1783ff1f7cb) you can find the full description of the two challenges available.