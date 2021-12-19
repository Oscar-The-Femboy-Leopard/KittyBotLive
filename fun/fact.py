import random
import discord
import datetime
from discord.ext import commands
from config import _blnk_value, Owner_Name

aliases = ['facts', 'randfact', 'Random_Fact']
description = "It gives out a random fact!"


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=aliases,
                      description=description)
    async def fact(self, ctx):
        fact = [
                'The scientific term for brain freeze is “sphenopalatine ganglioneuralgia”.',
                'Canadians say “sorry” so much that a law was passed in 2009 declaring that an apology can’t be used as evidence of admission to guilt.',
                'Back when dinosaurs existed, there used to be volcanoes that were erupting on the moon.',
                'The only letter that doesn’t appear on the periodic table is J.',
                'One habit of intelligent humans is being easily annoyed by people around them, but saying nothing in order to avoid a meaningless argument.',
                'If a Polar Bear and a Grizzly Bear mate, their offspring is called a “Pizzy Bear”.',
                'In 2006, a Coca-Cola employee offered to sell Coca-Cola secrets to Pepsi. Pepsi responded by notifying Coca-Cola.',
                'There were two AI chatbots created by Facebook to talk to each other, but they were shut down after they started communicating in a language they made for themselves.',
                'Nintendo trademarked the phrase “It’s on like Donkey Kong” in 2010.',
                'Daniel Radcliffe was allergic to his Harry Potter glasses. He had an allergy to nickel, and they were quickly replaced with hypoallergenic specs.\n\nAlso, did you know that his glasses had no lenses? This was to stop the reflection from anything happening behind the scenes. The glass lens was added in post-production.',
                'The famous line in Titanic from Leonardo DiCaprio, “I’m king of the world!” was improvised.',
                'A single strand of Spaghetti is called a “Spaghetto”.',
                'Hershey’s Kisses are named that after the kissing sound the deposited chocolate makes as it falls from the machine on the conveyor belt.',
                'Princess Peach - from Mario - didn’t move until 1988, designers believed it was too complicated to make her a movable character.',
                'To leave a party without telling anyone is called in English, a “French Exit”. In French, it’s called a “partir à l’anglaise”, to leave like the English.',
                'If you cut down a cactus in Arizona, you’ll be penalized up to 25 years in jail.It is similar to cutting down a protected tree species.',
                'The Buddha commonly depicted in statues and pictures is a different person entirely.The real Buddha was actually incredibly skinny because of self - deprivation.',
                'In Colorado, USA, there is still an active volcano. It last erupted about the same time as the pyramids were being built in Egypt.',
                'The first movie ever to put out a motion-picture soundtrack was Snow White and the Seven Dwarves.',
                "If you point your car keys to your head, it increases the remote’s signal range. If you point your car keys to your head, it increases the remote's signal range. This works by using your brain to act as a radio transmitter.",
                'Fruit stickers are edible, though the same with any fruit, washing prior to eating is recommended. The glue used for them is regulated by the FDA.',
                'The scientific name for Giant Anteater is Myrmecophaga Tridactyla. This means “ant eating with three fingers”.',
                'Astronaut is a compound word derived from the two Ancient Greek words “Astro” meaning “star” and “naut” meaning “sailor”. So astronaut literally means “star sailor”.',
                'The flashes of colored light you see when you rub your eyes are called “phosphenes”.',
                'At birth, a baby panda is smaller than a mouse.',
                'Iceland does not have a railway system.',
                'The largest known prime number has 17,425,170 digits. The new prime number is 2 multiplied by itself 57,885,161 times, minus 1.',
                'Forrest Fenn, an art dealer and author, hid a treasure chest in the Rocky Mountains worth over 1 million dollars. It still has not been found.',
                'The lead singer of The Offspring started attending school to achieve a doctorate in molecular biology while still in the band. He graduated in May 2017.',
                'The world’s largest grand piano was built by a 15-year-old in New Zealand. The world’s largest grand piano was built by a 15-year-old in New Zealand. The piano is a little over 18 feet long and has 85 keys – 3 short of the standard 88.',
                'The tongue is the only muscle in one’s body that is attached from one end.',
                'There is a company in Japan that has schools that teach you how to be funny. The first one opened in 1982. About 1,000 students take the course each year.',
                'The Lego Group is the world’s most powerful brand. There are more Lego minifigures than there are people on Earth.',
                'The Bagheera kiplingi spider was discovered in the 1800’s and is the only species of spider that has been classified as vegetarian.',
                'There is a boss in Metal Gear Solid 3 that can be defeated by not playing the game for a week; or by changing the date.',
                'The Roman – Persian wars are the longest in history, lasting over 680 years. They began in 54 BC and ended in 628 AD.',
                'Elvis was originally blonde. He started coloring his hair black for an edgier look. Sometimes, he would touch it up himself using shoe polish.',
                'If you translate “Jesus” from Hebrew to English, the correct translation is “Joshua”. The name “Jesus” comes from translating the name from Hebrew, to Greek, to Latin, to English.',
                'Ed Sheeran bought a ticket to LA with no contacts. He was spotted by Jamie Foxx, who offered him the use of his recording studio and a bed in his Hollywood home for six weeks.',
                'German Chocolate Cake is named after an American baker by the name of Samuel German. German Chocolate Cake is named after an American baker by the name of Samuel German. It has has no affiliation with the country of Germany.',
                'The first service animals were established in Germany during World War I. References to service animals date as far back as the mid-16th Century.',
                'An 11-year-old girl proposed the name for Pluto after the Roman god of the Underworld.',
                'The voice actor of SpongeBob and the voice actor of Karen, Plankton’s computer wife, have been married since 1995.',
                'An Italian banker, Gilberto Baschiera is considered a modern-day Robin Hood. Over the course of 7 years, he secretly diverted 1 million euros to poorer clients from the wealthy ones so they could qualify for loans. He made no profit and avoided jail in 2018 due to a plea bargain.',
                'Octopuses and squids have beaks. The beak is made of keratin – the same material that a bird’s beak, and our fingernails are made of.',
                'An estimated 50% of all gold ever mined on Earth came from a single plateau in South Africa: Witwatersrand.',
                '75% of the world’s diet is produced from just 12 plant and five different animal species.',
                'The original Star Wars premiered on just 32 screens across the U.S. in 1977. This was to produce buzz as the release widened to more theaters.',
                'The British government coined the slogan, “Keep Calm and Carry on” during World War 2 in order to motivate citizens to stay strong.',
                'Apple paid a couple $1.7 million dollars for their plot of land, which was only worth $181,700. While Apple was building a huge data center in the middle of North Carolina, they wanted to occupy the area of a couple that lived there for 34 years. When the couple refused to leave, Apple paid them $1.7 million dollars for their land.',
                'Tirana, the capital of Albania has a lot of things in common with other European capitals – except one.  It’s one of two capitals without a McDonalds. The second is Vatican City.',
                'Sour Patch Kids are from the same manufacturer as Swedish Fish. The red Sour Patch Kids are the same candy as Swedish Fish, but with sour sugar.',
                'The largest Japanese population outside of Japan stands at 1.6 million people who live in Brazil.',
                'IKEA is an acronym which stands for Ingvar Kamprad Elmtaryd Agunnaryd, which is the founder’s name, farm where he grew up, and hometown.',
                'In 2009, Stephen Hawking held a reception for time travelers, but didn’t publicize it until after. This way, only those who could time travel would be able to attend. Nobody else attended.',
                'Violin bows are commonly made from horse hair.',
                'There are less than 30 ships in the Royal Canadian Navy which is less than most third-world countries.',
                'Larry the Cable Guy’s real name is Daniel Lawrence Whitney. His notable Southern accent is fake – he was born and raised in the mid-west, not the South.',
                'The youngest Pope in history was Pope Benedict IX who was 11 years old at the time of election. He is also the only person to have been the Pope more than once.',
                'There were only 9 developers on the team for GoldenEye 007 for Nintendo 64. Goldeneye 007 - Nintendo 64 Only one of the developers had ever worked on a video game before.\n\n\ The game received multiple year-end awards, including the BAFTA Interactive Entertainment Games Award in 1998, and four awards from the inaugural AIAS Interactive Achievement Awards.',
                'Costa Coffee employs Gennaro Pelliccia as a coffee taster, who has had his tongue insured for £10 million since 2009.',
                'Johnny Cash took only three voice lessons before his teacher advised him to stop taking lessons and to never deviate from his natural voice.',
                'There is an island called “Just Enough Room”, where there’s just enough room for a tree and a house.',
                'People who post their fitness routine to Facebook are more likely to have psychological problems.',
                'Medieval chastity belts are a myth. A great majority of examples now existing were made in the 18th and 19th centuries as jokes.',
                'Nowadays, millionaires with just $1 million isn’t considered wealthy anymore by most Americans. Now, the typical American sees at least $2.4 million as wealthy.',
                'Hanna-Barbera pitched The Flintstones to networks for 8 weeks before it was finally picked up. It became the first ever animated show to air during primetime.',
                'There is a company that sells mirrors that make people look 10 pounds thinner. Overall, the mirrors have contributed to 54% of total sales for retailers that use it.',
                'There’s no period in “Dr. Pepper”. It was removed because the old logo font made it look like “Di: Pepper”.',
                'There is an underwater version of rugby, unsurprisingly called “underwater rugby”. It is a contact sport between 2 teams of 6 competing underwater in a pool to score goals while freediving.',
                'Standing around burns calories. On average, a 150 pound person burns 114 calories per hour while standing and doing nothing.',
                'Although GPS is free for the world to use, it costs $2 million per day to operate. The money comes from American tax revenue.',
                'In World War II, Germany tried to collapse the British economy by dropping millions of counterfeit bills over London.',
                'The human eye is so sensitive that, if the Earth were flat and it was a dark night, a candle’s flame could be seen from 30 miles away.',
                'When Space Invaders was created, Tomohiro Nishikado left in the lag caused by more invaders on the screen in order to create greater difficulty in the games.',
                'The color red doesn’t really make bulls angry; they are color-blind.',
                '65% of autistic kids are left-handed, and only 10% of people in general are left-handed.',
                'In 2007, Scotland spent £125,000 devising a new national slogan. The winning entry was: “Welcome to Scotland”.',
                'Until 2016, the “Happy Birthday” song was not for public use. Meaning, prior to 2016, the song was copyrighted and you had to pay a license to use it.',
                'When mice live in the wild, they typically only live for about six months. This is mostly due to the fact that the’re a good source of food for other animals. However, in a controlled environment like being kept as a pet, they can live up to two years.',
                'Lettuce is a member of the sunflower family.',
                'Researches have found that flossing your teeth can help your memory. Flossing prevents gum disease, which prevents stiff blood vessels, which cause memory issues.',
                'A cluster of bananas is called a “hand”. Along that theme, a single banana is called a “finger”.',
                'The Hobbit has been published in two editions. In the first edition, Gollum willingly bet on his ring in the riddle game.',
                'For nearly 60 years, Texas didn’t have an official state flag between 1879 & 1933. During that time, the Lone Star flag was the active, but unofficial flag.',
                'A wildlife technician, Richard Thomas, took the famous tongue twister, “how much wood would a woodchuck chuck if a woodchuck could chuck wood” and calculated a rough estimate of what the answer would actually be. It came out to be around 700 pounds.',
                'Red Solo cups are a common souvenir to bring back from the United States. The novelty comes from the cups being used in many party scenes in movies.',
                'Swedish meatballs originated from a recipe King Charles XII brought back from Turkey in the early 1800s.',
                'Saint Lucia is the only country in the world named after a woman. The country was named after Saint Lucy of Syracuse by the French.',
                'Those cute furry bits inside a cat’s ear are called “ear furnishings”. They ensure that dirt doesn’t go inside and also helps them to hear well.',
                'Scientists discovered sharks that are living in an active underwater volcano. Divers cannot investigate because they would get burns from the acidity and heat.',
                'There are times when Pluto is closer to the Sun than Neptune – one of these timelines was from 1979 to 1999.',
                'There is a town in Nebraska called Monowi with a population of one. The only resident is a woman who is the Mayor, Bartender and Librarian.',
                'The Ethiopian calendar is 7.5 years behind the Gregorian calendar due to the fact that it has 13 months.',
                'In 1994, the company who had a patent on GIFs tried to charge a fee for using GIFS. The PNG was invented as an alternative, and the company backed down.',
                'China is spending $3 billion dollars to build panda shaped solar farms in order to get more young people interested in renewable energy.',
                'Mercury and Venus are the only two planets in our solar system that do not have any moons.',
                'The average American child is given $3.70 per tooth that falls out.',
                'To properly write adjectives in order, you would list them by amount, value, size, temperature, age, shape, color, origin, and material.'

        ] #this is 1 to 100 on https://www.thefactsite.com/1000-interesting-facts/. Need to add the others

        fact2 = [
                'The world’s first motel is in San Luis Obispo. Built in 1925. When opened, it cost $1.25 for a two-room bungalow with a kitchen and a private adjoining garage.',
                'Scotland was one of the few countries able to hold off being conquered by the Romans in the first century A.D.',
                'I Will Always Love You was originally written and recorded in 1973 by Dolly Parton. It was written as a farewell to her mentor of seven years.',
                '“Opposites attract” is a common myth. People are actually attracted to people who look like family members, or those with a similar personality type.',
                'Llamas can be used as guards against coyote attacks on sheep herds. Studies have proven that just one guard llama is an effective protector and can even kill the attacking coyotes.',
                'The unique smell of rain actually comes from plant oils, bacteria, and ozone.',
                'Vanilla flavoring is sometimes made with the urine of beavers.',
                'If you heat up a magnet, it will lose its magnetism.',
                'The most expensive virtual object is “Club NEVERDIE” in the Entropia Universe which is worth $635,000. It was originally bought at $10,000.',
                'Cruise ships have morgues that can store up to 10 bodies at once. The average amount of people that die on cruise ships per year is 200.',
                'Birds are the closest living relatives of crocodilians, as well as the descendants of extinct dinosaurs with feathers. This makes them the only surviving dinosaurs.',
                'Small as they may be, ladybugs have a unique smell that humans are incredibly sensitive to.',
                'During WWII, a U.S. naval destroyer won a battle against a Japanese submarine by throwing potatoes at them. The Japanese thought they were grenades.',
                'The Marshal Mathers foundation for at-risk and disadvantaged youth, was founded by Eminem.',
                'A man with severe OCD and a phobia of germs attempted to commit suicide with a gun to his head. Instead of killing him, the bullet eliminated his mental illness without any other damage.',
                'Since 1955, 50% of the population of Niger is consistently under 16 years old. The total current population is 21,600,000.',
                'The author of Mary Had a Little Lamb, Sarah Josepha Hale, is most responsible for the creation of Thanksgiving being a national holiday.',
                'The oldest unopened bottle of wine was found in a Roman tomb that is over 1,650 years old.',
                'Chicken Run is the highest-grossing stop motion animated film, even beating The Nightmare Before Christmas.',
                'Nobody knows how the Academy Awards came to be referred to as the Oscars. The earliest mention was 1932, and was made official in 1939.',
                'More tornadoes occur in the United Kingdom per square mile than any other country in the world.',
                'Owners of personalized license plates in Uganda are facing a tax increase of over 300%, which will raise the tax from $1,498 to $5,992.',
                'Popularized by the Shakespeare play, many people think Julius Caesar’s last words were “And you, Brutus?” In reality, he said “You too, my child?”',
                'Times Square was originally called Longacre square until it was renamed in 1904 after The New York Times moved its headquarters to the newly built Times Building.',
                'Daniel Craig was an anonymous Storm Trooper in Star Wars: The Force Awakens. Originally, he denied his cameo and claimed he wouldn’t bother being an extra in a movie.',
                'Queen Elizabeth has a personal net worth of 425 million dollars. That includes the $65 million Sandringham House and $140 million Balmoral Castle.',
                'Although there is currently no drug proven to make someone tell the truth, some countries like Russia, Canada, and India use truth serums.',
                'Only primates, humans, and opossums have opposable thumbs. Out of these, the opossum is the only one with no thumbnail.',
                'One of the World Trade Center’s was built to be 1,776 feet tall on purpose to reference the year the Declaration of Independence was signed.',
                'The word “kimono”, literally means a “thing to wear”. Ki is “wear”, and mono is “thing”.',
                'There is a statue of Tesla in Silicon Valley that radiates free Wi-Fi. It was done as an homage to his vision for wireless communication.',
                'It snows metal on planet Venus! There are two types that have been found, galena and bismuthinite.',
                'Tic Tacs got their name from the sound they make when they are tossed around in their container.',
                'Only official members of a federally accepted Native American tribes may legally possess or collect eagle feathers. If a normal citizen has one, it is illegal.',
                'By the time they have been retired for 2 years, 78% of former NFL players have gone bankrupt or are under financial stress because of joblessness or divorce.',
                '500 seeds of 5 different types of seeds were taken into orbit around the moon, and later planted around the U.S. as well as a few countries. They were called Moon Trees.',
                'In order to protest the high tariffs enforced by a U.K. censorship board, a filmmaker sent in a 10 hour “movie” of white paint drying. They had to watch the entire film.',
                'The popular LMFAO group who created the viral hit, Party Rock Anthem, is made up of an uncle-nephew duo.',
                '50% of apartments in Los Angeles don’t come with a fridge. This is legal, as fridges are considered an “amenity”, and therefore landlords are not required to provide one.',
                'Norway has a 25 year statute of limitation on murder. This means if the murder happened more than 25 years ago, they cannot be charged.',

                ] #This is numbers 101 to 140 from the same website

        chooseFact = random.choice([fact, fact2])
        response = random.choice(chooseFact)
        color = discord.Color.dark_red()
        msg = ctx
        guild = msg.guild

        q = discord.Embed(color=color, timestamp=datetime.datetime.utcnow())
        q.add_field(name=_blnk_value, value=response, inline=True)
        q.set_footer(text=f'Bot made by {Owner_Name}')

        await ctx.send(embed=q)

        # await ctx.send(f'> Question: {question}\n Response: {random.choice(_8ball_responses)}')  # Sends response


def setup(client):  # Sets up the client for the client
    client.add_cog(Fun(client))  # Adds the command to the client for it to be able to run
