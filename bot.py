# Copyright (c) 2018 Alaa BEN JABALLAH

import sys
import traceback
from nlp.rasa import RasaNLP
from dataprovider.dataprovider import DataProvider

try:
	dp = DataProvider()

	r = RasaNLP(dp, "./modelDB/rasa-config.json", "./modelDB/rasa-data.json", "./rasa-model")
	r.train()

	while True:
		prenom = input(">> You say : ")
		text_to_reply = r.find_reply(prenom)
		print("<< Bot Answer : {}".format(text_to_reply))

except KeyboardInterrupt:
	r.snapshot_unparsed_messages("rasa-unparsed.txt")
	sys.exit(0)
except:
	r.snapshot_unparsed_messages("rasa-unparsed.txt")
	traceback.print_exc()