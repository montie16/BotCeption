from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

train = [
    ('I love this sandwich.', 'pos'),
    ('This is an amazing place!', 'pos'),
    ('I feel very good about these beers.', 'pos'),
    ('This is my best work.', 'pos'),
    ("What an awesome view", 'pos'),
    ('I want to eat','pos'),
    ('Hanging out with friends','pos'),
    ('Had a wonderful night out last night','pos'),
    ('Their food was amazing','pos'),
    ('I do not like this restaurant', 'neg'),
    ('Breaking news come check out http:/','neg'),
    ('I am tired of this stuff.', 'neg'),
    ("I can't deal with this", 'neg'),
    ('He is my sworn enemy!', 'neg'),
    ('Check out this wepage','neg'),
    ('Check out these photos','neg'),
    ('Lose weight fast','neg'),
    ('Listen to my','neg'),
    ('Follow this link','neg'),
    ('My boss is horrible.', 'neg'),
    ('Check out these celebrities','neg'),
    ('Hello World!','neg'),
    ('Hows the day going','pos'),
    ('would you care to hear some special deals','neg'),
    ('The new Iphone sucks','pos'),
    ('I love my android phone', 'pos'),
    ('Ferguson case','pos'),
    ('Hey boys wanna know a secret','neg'),
    ('Find out the top sexy models','neg'),
    ('Check this link for lovely looking ladies','neg'),
    ('This is where you go to lose weight','neg'),
    ('I was able to add weight to my lift','pos'),
    ('RT @username: ','neg'),
    ('#holla #Ferguson #cool','pos'),
    ('Adorable pic.twitter.com','neg'),
    ('pic.twitter.com','neg'),
    ('Kenny Hill be like pic.twitter.com','pos'),
    ('Did you see the football game last week?','pos'),
    ('Did you see the football game last night?','pos'),
    ('Did you see the football game?','pos'),
    ('Find out what your look alike celebrity is','neg'),
    ('Did you see the look on their faces #priceless','pos'),
    ('Interrupt my sleep and Ill Interrupt your breathing','neg'),
    ('@username want to go play soccer tonight','pos'),
    ('@username wanna go shoot some hoops','pos'),
    ('Whoop','pos'),
    ('Are people really this stupid?','pos'),
    ('Found out how you can get followers now','neg'),
    ('Come to this link to see Real celebrities lose weight fast, and how they did it','neg'),
    ('#deal','neg'),
    ('#sale','neg'),
    ('#sexyimage','neg'),
    ('#sexylook','neg'),
    ('Save big with us today','neg'),
    ('Lifted so much weight today','pos'),
    ('Squatted so much weight today','pos'),
    ('Love me some Leg Days','pos'),
    ('I love my Girlfriend','pos'),
    ('I love my Boyfriend','pos'),
    ('I love to eat so much food','pos'),
    ('Merry Christmas to everyone','pos'),
    ('Hope you have a wonderful day today, because I am','pos'),
    ('I hate when people ignore me','pos'),
    ('I got so trashed last night','pos'),
    ('Got a girls number last night','pos'),
    ('The bar was super packed','pos'),
    ('it was such a great time', 'pos'),
    ('Follow me and Ill follow you back','neg'),
    ('#follow','neg'),
    ('Im laughing so hard at this right now tinyurl.com/','neg'),
    ('Do u ever','neg'),
    ('You want 2','neg'),
    ('RT @username: I LOL at this so much','neg'),
    ('RT @username: I had a great time last night', 'pos'),
    ('vine.co','neg'),
    ('That goal was sick! vine.co','pos'),
    ('This video was so hilarious when I found it vine.co','pos'),
    ('RT @username: come check out my page','neg'),
    ('Learn the secrets behind looking leaner','neg'),
    ('Get muscular in just 30 days','neg'),
    ('follw me please','neg'),
    ('I got high as a kite last night','pos'),
    ('How I met your mother is the best show ever','pos'),
    ('SOA was insane','pos'),
    ('SOA I cant believe that just happened','pos'),
    ('Check out Kim kardashians new look','neg'),
    ('Check out this celebrities new look','neg'),
    ('I hate doing math homework, but I like procrastinating','pos'),
    ('I hear people running around above me','pos'),
    ('Find out the new "in" look','neg'),
    ('Where is waldo','pos'),
    ('RT @username: what do you think of this page?','neg'),
    ('I had a great time gonig out with some awesome friends','pos'),
    ('Getting too turnt','pos'),
    ('#drunk','pos'),
    ('#crazy #randomcrap','pos'),
    ('Its time to party hard!','pos'),
    ('what r u doing','pos'),
    ('come find ur favorite celebrity','neg'),
    ('u 2 can become lean','neg'),
    ('Lost my phone last night','pos'),
    ('That girl last night looked so Ratchet','pos'),
    ('Porn Star "Vicky Pattison" reveals how she went from Ratchet to Fantastic','neg'),
    ('Turn from Ratchet to Fantastic','neg'),
    ('check out this sick picture from last night out bit.ly','pos'),
    ('bit.ly','neg'),
    ('The most funny sex selfies bit.ly','neg'),
    ('@username: has some of the funniest tweets ever','neg'),
    ('Holy crap @username that was so hilarious','pos'),
    ('How to increase your breast size in a matter of weeks','neg'),
    ('Let it go, let it go! Frozen','pos'),
    ('@username check out this funny ass video www.youtube.com','pos'),
    ('I had sex with someone last night','pos'),
    ('Ways to improve sex','neg'),
    ('sex positions','neg'),
    ('Movie night with Bae','pos'),
    ('That was such a great movie last night #Legit #Action','pos'),
    ('Great night with this one instagram.com/','pos'),
    ('these people I swear pic.twitter.com','pos'),
    ('@username @username we gotta go check out this burger joint sometime','pos'),
    ('Buy this product and get the second one free','neg'),
    ('Losing weight is such a pain, I would rather just eat','pos'),
    ('Lose weight like these hot celebrities','neg'),
    ('The secret to looking thin isnt as hard as you think, check out these hot models secrets','neg'),
    ('Learn secret of the most productive people','neg'),
    ('aboutgoals.com','neg'),
    ('Tony Romo has homosexual relations, check it out now','neg'),
    ('did you check out this new song www.youtube.com/','pos'),
    ('have you seen the news about the Texas?','pos'),
    ('have you seen how Tony Romo is doing?','pos'),
    ('Adrian Peterson is back, and not abusing anyone','pos'),
    ('working on this table #woodworking','neg'), #This is a bot account about just woodworking...really
    ('Kelly Osbourne & other celebs are using this diet to lose weight!','neg'),
    ('someone hit me up, im bored','pos'),
    ('Hello, Please follow me! It would mean the world','neg'),
    ('Hello, please follow me','neg'),
    ('Star wars Force Awakens is going to be so SICK','pos'),
    ('days until ','pos'),
    ('Clutch move on my part','pos'),
    ('That play was so clutch','pos'),
    ('cant wait to go hunting','pos'),
    ('#fitness','neg'),
    ('#workout','neg'),
    ('I love to be in shape #fitness','pos'),
    ('hitting the gym hard today was the best #workout','pos'),
    ('join us','neg'),
    ('join us at shredzville.com','neg'),
    ('mainstreambullspit.com','neg'),
    ('This black friday sale is unreal, check it out','neg'),
    ('went black firday shopping and never again will I do it','pos'),
    ('Black friday shopping was great and I got so much crap for so little','pos'),
    ('I feel as if im the only one drinking on a monday night`','pos'),
    ('Going to sixth street its going to be a blast','pos'),
    ('So many people taking selfies these days','pos'),
    ('I get the weirdest selfies snapchats on the face of this planet','pos'),
    ('snapchat','pos'),
    ('facebook','pos'),
    ('instagram','pos'),
    ('Sell your iphone or Android device here','neg'),
    ('when did you want to go lift?','pos'),
    ('Eating healthy is the best way to keep a healthy body','pos'),
    ('I really dont want to study today','pos'),
    ('I hate school work so much','pos'),
    ('This class is the best','pos'),
    ('This classes professor is the best, but class sucks','pos'),
    ('Thic class and professor are the best','pos'),
    ('This professor is the best','pos'),
    ('This professor isnt cool, but his class is','pos'),
    ('The secrets to','neg'),
    ('how to increase your workout performance','neg'),
    ('Studies show that sexual performance can','neg'),
    ('Come eat our meals for buy one get one','neg'),
    ('New free app, where you can make money','neg'),
    ('Easy way to make money fast','neg'),
    ('doing it in public','neg'),
    ('@username ill follow you if youd like','neg'),
    ('Some people are so silly','pos'),
    ('I dont ever use my twitter account','pos'),
    ('What happened last night?','pos'),
    ('Dude wheres my car','pos'),
    ('This new video game is so sick','pos'),
    ('its time to stop monkeying around','pos'),
    ('Time to play ball','pos'),
    ('Watch athlete break the law','neg'),
    ('cbsn.ws','neg'),
    ('abcn.ws','neg'),
    ('Come on you can do it','pos'),
    ('@username @username @username','pos'),
    ('@username @username','pos'),
    ('@username @username last weekend though','pos'),
    ('I love cookies','pos'),
    ('Watching pokemon reminds me of my youth','pos'),
    ('playing pokemon is so great','pos'),
    ('Relationship goals','pos'),
    ('Relationship goals pic.twitter.com','neg'),
    ('This old man and women pic.twitter.com Relationship goals','pos'),
    ('Coming out of the closet was the hardest thing to do','pos'),
    ('I love my friends','pos'),
    ('I love my family','pos'),
    ('I have the best family ever','pos'),
    ('I have the most supportive friends','pos'),
    ('Why workout when you can do this','neg'),
    ('I love the gym when im alone','pos'),
    ('wokring out helps me focus on life','pos'),
    ('working late tonight','pos'),
    ('Working overtime is just the worst','pos'),
    ('Make money now and never work again','neg'),
    ('the secret to success is here','neg'),
    ('click the link above','neg'),
    ('subscribe to us now, and we shall follow you','neg'),
    ('I made a loud fart in class today','pos'),
    ('everyone is looking at me','pos'),
    ('I know @username little secret','pos'),
    ('I know a secret','pos'),
    ('That guy was so buff','pos'),
    ('That girl was ripped','pos'),
    ('2 dollar drafts','pos'),
    ('public celeb weight loss trick','neg'),
    ('ges leaked across the web','neg'),
    ('Why does suddenlink suck so bad','pos'),
    ('When Wifi is down, my life is ruined','pos'),
    ('Sorry, I dont speak cunt','neg'),
    ('Anyone who charges you money for anything is ripping you off','neg'),
    ('when u drop ur phone on face pic.twitter.com','neg'),
    ('What beer do I want','pos'),
    ('I dropped my phone in the toilet','pos'),
    (':D','pos'),
    (':(','pos'),
    (':)','pos'),
    ('These gains come from hard work and determination','pos'),
    ('find out your crush here','neg'),
    ('Who is your celebrity crush','neg'),
    ('where should I go tonight','pos'),
    ('Titties','pos'),
    ('getting flashed is such an experience','pos'),
    ('Dude that girl looked so ratchet last night','pos'),
    ('Christmas shopping','pos'),
    ('Going to be an uncle','pos'),
    ('My nephew is just the cutest','pos'),
    ('Im going to be a mother','pos'),
    ('Im going to be a father','pos'),
    ('Frat guys are a joke','pos'),
    ('Frt guys are assholes','pos'),
    ('sorority girls dont ever wear pants','pos'),
    ('sorority girls always have drama','pos'),
    ('Ring dunks','pos'),
    ('Getting my ring today','pos'),
    ('Hobbit the five armies','pos'),
    ('calculus was a blast','pos'),
    ('trying to find twitter bots','pos'),
    ('peace','pos'),
    ('life struggles','pos'),
    ('laying in bed','pos'),
    ('comfy pants','pos'),
    ('fashion disaster of this celebrities','neg'),
    ('Mike Evans','pos'),
    ('Johnny Manziel','pos'),
    ('Texas A&M football','pos'),
    ('Barclays premier league','pos'),
    ('But gear now at www.worldsoccershop.com','neg'),
    ('shop at EarlDibblesJr.com','neg'),
    ('Hoodies 50% off','neg'),
    ('up to 30% off','neg'),
    ('up to 75% off','neg'),
    ('New gear avaialbe here','neg'),
    ('I cant hear my music','pos'),
    ('Jamming my new beats','pos'),
    ('Dr. Dre','pos'),
    ('Can today end','pos'),
    ('Taco Bell','pos'),
    ('Whataburger','pos'),
    ('Panda Express','pos'),
    ('Sibisa','pos'),
    ('ChickFilA','pos'),
    ('New Burritos $1 Taco Bell','neg'),
    ('I want','pos'),
    ('I like to eat','pos'),
    ('Lose weight, while eating what you want','neg'),
    ('buy this supplement now','neg'),
    ('I wish I had','pos'),
    ('I wish','pos'),
    ('I have ','pos'),
    ('This just in:','neg'),
    ('That live performance was phenomenal','pos'),
    ('ESPN showing the best game ever','pos'),
    ('Google is my best friend','pos'),
    ('find out who views your twitter profile','neg'),
    ('Come shop with us today','neg'),
    ('earn money without work','neg'),
    ('losing weight made easy with these 5 steps','neg'),
    ('It takes me months to lose weight','pos'),
    ('Phone calls','pos'),
    ('call now to win','neg'),
    ('bae','pos'),
    ('Cristiano Ronaldo','pos'),
    ('Why did I lose power','pos'),
    ('bought a new computer today','pos'),
    ('Get the internet youve dreamed about here','neg'),
    ('buy a new computer today','neg'),
    ('secret life of ','neg'),
    ('Mexican food','pos'),
    ('College cup','pos'),
    ('SEC championship','pos'),
    ('La Liga','pos'),
    ('Fantastic performance by the team','pos'),
    ('watch this stream twith.tv','pos'),
    ('Come check out our deals amazon.com','neg'),
    ('AT&T deals now','neg'),
    ('att.com','neg'),
    ('new flash sales newegg.com','neg'),
    ('puppy','pos'),
    ('kitten','pos'),
    ('I got a ring','pos'),
    ('aggie ring','pos'),
    ('deals on rings','neg'),
    ('deals on pets','neg'),
    ('cat accessories for sale','neg'),
    ('cat video','pos'),
    ('screw finals','pos'),
    ('Finals week','pos'),
    ('Procrastination at its finest','pos'),
    ('Procrastination','pos'),
    ('sneezing','pos'),
    ('I hate ','pos'),
    ('I love ','pos'),
    ('I found','pos'),
    ('Craving something','pos'),
    ('Coffee','pos'),
    ('Starbucks','pos'),
    ('Get a $5 off starbucks','neg'),
    ('Fantasy football','pos'),
    ('Basketball','pos'),
    ('Baseball','pos'),
    ('Swimming and Diving','pos'),
    ('buy sports gear','neg'),
    ('college is crazy','pos'),
    ('University is better than work','pos'),
    ('What is life','pos'),
    ('Why am i so bored','pos'),
    ('pushing people away','pos'),
    ('fuzzy socks','pos'),
    ('Cheeseburgers','pos'),
    ('I love sweater wheather','pos'),
    ('Zombie attacks','pos'),
    ('playing those video games','pos'),
    ('Steam','pos'),
    ('on Steam all night long','pos'),
    ('What happen last night @username','pos'),
    ('catch up on','pos'),
    ('watch movies','pos'),
    ('Start netflix','pos'),
    ('Netflix','pos'),
    ('The movie elf','pos'),
    ('Lost animal','pos'),
    ('share this please','neg'),
    ('If anybody needs me','pos'),
    ('I found love','pos'),
    ('I wish i was taller','pos'),
    ('Come support us','neg'),
    ('find out secret life of a celebrity','neg'),
    ('Must retweet','neg'),
    ('Type this discount code','neg'),
    ('Ah twitter you suck','pos'),
    ('Facebook is creep central','pos'),
    ('Santa Clause','pos'),
    ('Chocolate milk is best','pos'),
    ('Parks and Recs','pos'),
    ('This weeks top story','neg'),
    ('I just wanna drink','pos'),
    ('BOGO','neg'), #buy one get on free
    ('where you at','pos'),
    ('Find me and Ill find you','neg'),
    ('why do people complain so much','pos'),
    ('!!','pos'),
    ('#','pos'),
    ('my major','pos'),
    ('this semester','pos'),
    ('last semester','pos'),
    ('perfect','pos'),
    ('how to sculpt the perfect body','neg'),
    ('new gear found here','neg'),
    ('while loops','pos'),
    ('call me up a pizza @username','pos'),
    ('I want pizza','pos'),
    ('Buy a pizza, get one half off','neg'),
    ('boring','pos'),
    ('dating my friend','pos'),
    ('I dont know','pos'),
    ('sometimes you cant','pos'),
    ('playing xbox one','pos'),
    ('playing PS4','pos'),
    ('buy a PS4 here','neg'),
    ('buy a Xbox one here','neg'),
    ('stuff','pos'),
    ('Would you like me to help','pos'),
    ('help','pos'),
    ('get help here now','neg'),
    ('get help losing weight','neg'),
    ('Snapchat me at','pos'),
    ('follow me on instagram ill follow you','neg'),
    ('Tonight we dine like champs','pos'),
    ('We are victorious','pos'),
    ('Team won 1st place','pos'),
    ('supplement up to get shredded quick','neg'),
    ('I found a new life','pos'),
    ('bought a new car','pos'),
    ('bought a new house','pos'),
    ('bought a new pet','pos'),
    ('buy a new car here','neg'),
    ('find your dream pet here','neg'),
    ('find new houses here','neg'),
    ('is this what your dream house looks like?','neg'),
    ('take this link','neg'),
    ('I found this link youd probably laugh at','pos'),
    ('check out this videogamer','pos'),
    ('when snapchat fails','pos'),
    ('creating the most intense food','pos'),
    ('cook like a cheif in no time, secrets how here','neg'),
    ('need my coffee','pos'),
    ('double expresso','pos'),
    ('ur','pos'),
    ('2','pos'),
    ('u','pos'),
    ('lol','pos'),
    ('lmao','pos'),
    ('Netflix is alright','pos'),
    ('Check out new Netflix deals','neg'),
    ('6 pack','pos'),
    ('poppin bottles','pos'),
    ('I had to poop so bad','pos'),
    ('poo','pos'),
    ('got sick as F last night','pos'),
    ('F','pos'),
    ('Fuck','pos'),
    ('Balls','pos'),
    ('Bitch','pos'),
    ('I made out with his Bitch','pos'),
    ('got fucked up','pos'),
    ('UFC','pos'),
    ('UFC fighting ','pos'),
    ('pay per view now','neg'),
    ('secret to win any fight','neg'),
    ('Ketchup','pos'),
    ('Mustard','pos'),
    ('make me a sandwich women','pos'),
    ('issues','pos'),
    ('Stage 5 clinger','pos'),
    ('she was','pos'),
    ('she is','pos'),
    ('he is','pos'),
    ('he was','pos'),
    ('your gonna love our offers','neg'),
    ('youll never regert buying from us','neg'),
    ('your able to lose weight in just 30 days','neg'),
    ('try our secret now your not gonna regret it','neg'),
    ('Find your soulmate here','neg'),
    ('match.com','neg'),
    ('where is my food','pos'),
    ('proud parent','pos'),
    ('Graduation','pos'),
    ('pround family member','pos'),
    ('well damn','pos'),
    ('people talking shit','pos'),
    ('Howdy!','pos'),
    ('howdy','pos'),
    ('lazy ass','pos'),
    ('what an asshole','pos'),
    ('lose weight now','neg'),
    ('get a personal trainer today','neg'),
    ('Im a personal trainer','pos'),
    ('locally hosting','pos'),
    ('Amazing support','pos'),
    ('just for $ you can have this','neg'),
    ('find top 5 best selfies','neg'),
    ('Dominoes','pos'),
    ('bored snapchatting away','pos'),
    ('to be or not to be','pos'),
    ('your not going to want to miss this deal','neg'),
    ('what you get','pos'),
    ('I dont get it','pos'),
    ('waffles','pos'),
    ('Bacon','pos'),
    ('proud','pos'),
    ('America','pos'),
    ('Beer','pos'),
    ('simple','pos'),
    ('people ignoring me','pos'),
    ('Never get ignored again!','neg'),
    ('Finally home','pos'),
    ('Finally graduated','pos'),
    ('Try online college now','neg'),
    ('A degree from home','neg'),
    ('Sports are fun','pos'),
    ('#NFL','pos'),
    ('#MLB','pos'),
    ('#NHL','pos'),
    ('#MLS','pos'),
    ('All nighter','pos'),
    ('Energy','pos'),
    ('Pure','pos'),
    ('Water','pos'),
    ('Im so thirsty','pos'),
    ('the struggle is real','pos'),
    ('Mount','pos'),
    ('Video streamming','pos'),
    ('Fluffy bunnies','pos'),
    ('You can get follwers quick','neg'),
    ('I found this deal, check it out','neg'),
    ('Find Motivation','pos'),
    ('Motivation','pos'),
    ('Stress','pos'),
    ('Finals are stressful','pos'),
    ('#stress','pos'),
    ('check out the top new trends','neg'),
    (':/','pos'),
    (':S','pos'),
    ('losing weight can be made fun, using these techniques','neg'),
    ('I foudn a dollar','pos'),
    ('Drugs are bad','pos'),
    ('what on earth','pos'),
    ('onion.com','neg'),
    ('Mario Kart','pos'),
    ('Super Smash','pos'),
    ('N64','pos'),
    ('Nintendo','pos'),
    ('ofa.bo','neg'),
    ('Imagine','pos'),
    ('Cartoon network','pos'),
    ('Transformation','pos'),
    ('fast car','pos'),
    ('run fast','pos'),
    ('how to run faster here','neg'),
    ('these shoes help you run faster','neg'),
    ('where can I find you','pos'),
    ('Dumb','pos'),
    ('Such a fail','pos'),
    ('contains','pos'),
    ('Ice cream','pos'),
    ('Find lifes secrets','neg'),
    ('stroms','pos'),
    ('thunderstorm','pos'),
    ('local news here','neg'),
    ('weight loss made simple','neg'),
    ('buy now','neg'),
    ('follow now','neg'),
    ('Ill follow you','neg'),
    ('Im a bot','neg'),
    ('I like creating website','pos'),
    ('I like Chocolate chips','pos'),
    ('I want chips','pos'),
    ('Who wants to play poker','pos'),
    ('Texas Holdem','pos'),
    ('21','pos'),
    ('turning 21 tomorrorw','pos'),
    ('21st birthday','pos'),
    ('21 is the best age','pos'),
    ('Happy birthday','pos'),
    ('Secrets dont make friends','pos'),
    ('RT','pos'),
    ('middle finger','pos'),
    ('Android','pos'),
    ('Microsoft','pos'),
    ('Apple','pos'),
    ('Comdey','pos'),
    ('Action','pos'),
    ('Scary','pos'),
    ('Horror','pos'),
    ('Adventure','pos'),
    ('1st person','pos'),
    ('3rd person','pos'),
    ('Iphone','pos'),
    ('Ipad','pos'),
    ('HP','pos'),
    ('Toshiba','pos'),
    ('ASUS','pos'),
    ('HTC','pos'),
    ('Nokia','pos'),
    ('Verizon','pos'),
    ('AT&T','pos'),
    ('Sprint','pos'),
    ('Go phone','pos'),
    ('phones','pos'),
    ('Best Buy','pos'),
    ('Best Buy deals','neg'),
    ('Numbers','pos'),
    ('Platforms','pos'),
    ('Android deals','neg'),
    ('check play store for these applications','neg'),
    ('apps','pos'),
    ('apps half off','neg'),
    ('Dollar','pos'),
    ('Get your Billion back America','neg'),
    ('Save your hard earned dollar with these helpful tips','neg'),
    ('You dropped something','pos'),
    ('These jeans will save you money','neg'),
    ('This deal will save you big','neg'),
    ('hot deals newegg.com','neg'),
    ('I know I will regret this','pos'),
    ('The hangover is real','pos'),
    ('So hungover','pos'),
    ('sell ticktets','neg'),
    ('Monday','pos'),
    ('Tuesday','pos'),
    ('wednesday','pos'),
    ('Thursday','pos'),
    ('Friday','pos'),
    ('Saturday','pos'),
    ('Sunday','pos'),
    ('Left hand','pos'),
    ('Right hand','pos'),
    ('Mother','pos'),
    ('Father','pos'),
    ('Find out your generation','neg'),
    ('I love to party','pos'),
    ('I hate partying','pos'),
    ('Never party alone, find out how to be cool','neg'),
    ('top 10 ways you know your cool','neg'),
    ('top 100 purchases you missed out on','neg'),
    ('I know all kinds of secrets','pos'),
    ('You cut me down','pos'),
    ('Love getting cut off','pos'),
    ('When an old person flips you off','pos'),
    (';','pos'),
    (',','pos'),
    ('I love my new heels','neg'),
    ('Hills','pos'),
    ('Climbing','pos'),
    ('check out these new in stock heels','neg'),
    ('whilest ','pos'),
    ('new victorias secret deals','neg'),
    ('Victorias secret','pos'),
    ('I love shopping at Victorias secret','pos'),
    ('gay','pos'),
    ('lesbian','pos'),
    ('pointless','pos'),
    ('never gain weight again, secrets here','neg'),
    ('fellow friends','pos'),
    ('to everyone reading this','pos'),
    ('we buy your gold','neg'),
    ('we buy your silver','neg'),
    ('Make money fast','neg'),
    ('I need a job','pos'),
    ('How do I get a job','pos'),
    ('I have an interview today!','pos'),
    ('!','pos'),
    ('Never knew youd be like that','pos'),
    ('new shoes','pos'),
    ('check out these deals on new shoes','neg'),
    ('not much difference','pos'),
    ('all the same','pos'),
    ('cleats','pos'),
    ('Check out new Nike','neg'),
    ('Check out a new Adidas','neg'),
    ('Maroon out','pos'),
    ('Gigem','pos'),
    ('I want pudding','pos'),
    ('Projects','pos'),
    ('coding is fun','pos'),
    ('lets game','pos'),
    ('we should get matching shoes','pos'),
    ('doe','pos'),
    ('dove hunting','pos'),
    ('skeet shooting','pos'),
    ('buy ammo online here','neg'),
    ('easy to follow weight losing','neg'),
    ('Solitare','pos'),
    ('when did I become','pos'),
    ('You left so early','pos'),
    ('Your so whipped','pos'),
    ('Ultimate Frisbee','pos'),
    ('Buy Frisbees here','neg'),
    ('I couldnt hear you','pos'),
    ('they weigh ounces','pos'),
    ('oz','pos'),
    ('lb','pos'),
    ('lbs','pos'),
    ('King kong','pos'),
    ('Gangster','pos'),
    ('Gangsta','pos'),
    ('Chains','pos'),
    ('Chainz','pos'),
    ('You dont have?','pos'),
    ('Are you still breathing?','pos'),
    ('breathing','pos'),
    ('Barrock Obama','pos'),
    ('George Bush','pos'),
    ('Bill Clinton','pos'),
    ('This just in Obama','neg'),
    ('This just in Bush','neg'),
    ('This just in Clinton','neg'),
    ('knee brace','pos'),
    ('Keystone','pos'),
    ('Shiner Bock','pos'),
    ('Coor Light','pos'),
    ('Bud Light','pos'),
    ('Miller','pos'),
    ('Samuel Adams','pos'),
    ('Come thirsty and grab a beer','neg'),
    ('just gained weight','pos'),
    ('I feel so fat','pos'),
    ('Ive lost so much weight','pos'),
    ('lost puppy','pos'),
    ('How cute is he','pos'),
    ('How cute is she','pos'),
    ('I got the number','pos'),
    ('@username bet you wont','pos'),
    ('no one else','pos'),
    ('Im all alone tonight','pos'),
    ('Super bored, someone hit me up','pos'),
    ('SOOOOOOOO bored','pos'),
    ('soooooooooooooo','pos'),
    ('haha','pos'),
    ('This made me lol','neg'),
    ('let me find out','pos'),
    ('@username I lost my ID last night','pos'),
    ('Last Friday night','pos'),
    ('RT: party over here','pos'),
    ('RT " "','pos'),
    ('Advertisment','neg'),
    ('Ads','neg'),
    ('Earn $ in the 1st month','neg'),
    ('Get your $ back','neg'),
    ('Bring a friend, get $','neg'),
    ('Give more Get more','neg'),
    ('Ready to Donate?','neg'),
    ('Help a child in need','neg'),
    ('Hit me up','pos'),
    ('Call me when you can','pos'),
    ('call me','pos'),
    ('your gonna love these cupcakes @username','pos'),
    ('deals','neg'),
    ('Cant hold your alcohol @username?','pos'),
    ('lets go hard tonight','pos'),
    ('why did we do that','pos'),
    ('what were we thinking?','pos'),
    ('Kevin Sumlin','pos'),
    ('Kyle Allen','pos'),
    ('Fightin Texas Aggies','pos'),
    ('Ags','pos'),
    ('Computer Science','pos'),
    ('Found a new recipe I like','pos'),
    ('Awesome','pos'),
    ('Lets play','pos'),
    ('Achievement Hunter','pos'),
    ('Are you famous, found out with this link','neg'),
    ('Someone bring me food','pos'),
    ('someone save me from boredom','pos'),
    ('going on a date night','pos'),
    ('dont do that @username','pos'),
    ('Ill help you find followers','neg'),
    ('Enter for a chance','neg')
]
test = [
    ('The beer was good.', 'pos'),
    ('I got so turnt', 'pos'),
    ('I do not enjoy my job', 'neg'),
    ("I ain't feeling dandy today.", 'neg'),
    ("I feel amazing!", 'pos'),
    ('Gary is a friend of mine.', 'pos'),
    ("I can't believe I'm doing this.", 'neg'),
    ('I want to eat Pancakes','pos'),
    ('Listen to my live stream','neg'),
    ('Great hanging out with my friends','pos'),
    ('Hey man you wanna go kick the ball around?','pos'),
    ('Aggie football was crazy lasy week','pos'),
    ('Check out this celebrities fast weight loss','neg'),
    ('check out how cute this puppy is pic.twitter.com','neg'),
    ('Found out I am getting a Bike for Christmas','pos'),
    ('This is so Adorable pic.twitter.com','neg'),
    ('hello world','neg'),
    ('Wanna know the secret to looking sexier in just 30 days?','neg'),
    ('5 Steps to gain followers quickly','neg'),
    ('@username, want to go play soccer?','pos'),
    ('Dude @username lets go grab a few drinks','pos'),
    ('Last nights game was amazing I scored 2 goals','pos'),
    ('Did you find your phone?','pos'),
    ('I had one of the best workouts today','pos'),
    ('Check out this vine.co 2 funny','neg'),
    ('The secret to losing weight in just 30 days','neg'),
    ('I will follow the next 100 to follw me','neg'),
    ('I am not a robot','neg'),
    ('RT @username: thanks for the foolow','neg'),
    ('This goal was sick vine.co','pos'),
    ('This was the most hilarious fail Ive ever seen www.youtube.com','pos'),
    ('Click here to see a secret weight loss technique you wont want to miss','neg'),
    ('Last night was awesome #drunk #tooturnt #turnup','pos'),
    ('Ways to boose your sex drive','neg'),
    ('How to pleasure your women the right way','neg'),
    ('Clcik this link to see crazy sex positions','neg'),
    ('Dude that chick I had sex with last night was a babe','pos'),
    ('They recommend this to you bit.ly/','neg'),
    ('This bar has some great deals tonight','pos'),
    ('Holy crap that play was clutch','pos'),
    ('I get the most random snapchats','pos'),
    ('@username Im gonna be honost that was all me','pos'),
    ('Duck hunting season is the best','pos'),
    ('Cant wait for dove hunting season','pos'),
    ('buy your hunting gear hear','neg'),
    ('ur post just scored you entry in our sweeps! click our header to claim','neg'),
    ('click our post to follow our link to our main page','neg'),
    ('have you seen this new weight loss program?','neg'),
    ('I want Taco Bell, Whataburger, or Mcdonalds','pos'),
    ('BOGO half off today only','neg'),
    ('Shop online for new hot deals','neg'),
    ('The secret in weight loss, allowing you to eat anything','neg'),
    ('Ill help you get followers if you follow me','neg'),
    ('get more followers now','neg'),
    ('Donate $ and you will gain money','neg'),
    ('Make money without working','neg'),
    ('Achieve more followers easily','neg'),
    ('I cant wait to go out tonight, its gonna be fun with @username','pos'),
    ('We went too hard last night','pos'),
    ('I think I got so drunk I blacked out','pos'),
    ('I cant wait to go to the gym, today ill work on my 6 pack','pos'),
    ('Working out and eating healthy is the best way to lose weight','pos'),
    ('You are so messed up','pos'),
    ('wanna grab a few beers tonight?','pos'),
    ('RT "Just know youre not alone, im gonna make this place your home"','pos'),
    ('I cant wait to order some food','pos'),
    ('go to amazon.com to check new hot deals','neg'),
    ('Saving made easy with this secret','neg'),
    ('Find out what celebrity you look like','neg'),
    ('find your soulmate at match.com','neg'),
    ('This just in:','neg'),
    ('where you wanna meet? @username','pos'),
    ('My fantasy team won today','pos'),
    ('My team scored so many points','pos'),
    ('That was the coolest goal ive ever seen','pos'),
    ('What a touchdown','pos'),
    ('Lets go Aggies! Gigem','pos'),
    ('This deal you wont want to miss','neg'),
    ('newegg.com hot deals','neg'),
    ('this made me lol vine.com','neg'),
    ('save money here','neg'),
    ('I cant seem to find a job, but I can get interviews','pos'),
    ('Enter for a chance to win $','neg')
    
]

c1 = NaiveBayesClassifier(train)
print("Sample Data sets")
print(c1.classify("@16Montie wanna go kick a ball?"))
print(c1.classify("I want Taco Bell"))
print(c1.classify("Earn up to $300 in the 1st month"))
print(c1.classify("How can I achieve more followers?"))
print


#stuff = raw_input('please type in Tweet ')
blob = TextBlob("Dude @ndy318 wanna go grab a drink, or ten #drunk.", classifier=c1)

                    
print(blob)
print(blob.classify())

for sentence in blob.sentences:
    print(sentence)
    print(sentence.classify())
    
print("The Accuracy: {0}".format(c1.accuracy(test)))

c1.show_informative_features(5)