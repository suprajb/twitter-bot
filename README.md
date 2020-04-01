# Twitter Bot

This is the code for a [twitter bot](https://twitter.com/the_hippie_tsar) that I made for fun. It aims to generate tweets mimicing the speech style of any person, using Markov chains (created using the excellent `markovify` module) for generative text.

## Run on your machine

Clone this repository using 
```bash
git clone https://github.com/youwishyouhadthishandle/twitter-bot.git
```
Install the requirements using 
```bash
pip install -r requirements.txt
```
To post a tweet, you'll need an API key provided to you after applying at https://developer.twitter.com/
Export the API keys to your environment using
```bash
export ACCESS_TOKEN=<your-access-token>
export ACCESS_SECRET=<your-access-secret>
export API_KEY=<your-consumer-api>
export API_SECRET=<your-api-secret>
```
and then run
```bash
python tweet.py
```


Note: The [language-check](https://pypi.org/project/language-check/) module requires a JVM to run.

## Mimic other people's rhetoric

The bot is customisable and can be used to tweet based on any corpus. The [data](./data) folder contains the courpus that the bot currently uses. To download quotes of a person to use as a corpus, run 
```bash
python get_quotes.py <name>
```
with the `<name>` replaced by the name of the person. This will download a .txt file to the directory specified in [helpers.py](./helpers.py) . You can then edit [tweet.py](tweet.py) accordingly. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
