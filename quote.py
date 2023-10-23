import psycopg2

# Establish database connection
conn = psycopg2.connect(
    host="localhost",
    database="postgres",
    user="postgres",
    password=""
)

# Create cursor
cursor = conn.cursor()

# Insert new data
quotes = content = [
('''True friends are like mirrors...;they reflect our true selves and provide honest feedback and support.''', 'FRIEND FACT'),
('''Friendship is a sanctuary...;a place where we find comfort, understanding, and acceptance.''', 'FRIEND FACT'),
('''Friendship is a journey...;it takes us on an adventure filled with shared experiences, growth, and memories.''', 'FRIEND FACT'),
('''Friendship is a tapestry of trust...;weaving together shared secrets, support, and unwavering belief in one another.''', 'FRIEND FACT'),
('''True friends are like guardian angels...;they watch over us, protect us, and offer guidance when we need it the most.''', 'FRIEND FACT'),
('''Friendship is a garden of joy...;nurturing each other with love, laughter, and shared moments of happiness.''', 'FRIEND FACT'),
('''Friendship is a treasure chest...;filled with precious memories, shared secrets, and unconditional support.''', 'FRIEND FACT'),
('''True friends are like puzzle pieces...;they fit together perfectly, creating a beautiful picture of support and understanding.''', 'FRIEND FACT'),
('''True friends are like stars in the night sky...;they illuminate our path and bring comfort to our souls.''', 'FRIEND FACT'),
('''Friendship is like a rainbow...;it adds color and beauty to our lives, reminding us of the joy of connection.''', 'FRIEND FACT'),
('''Friendship is a lifeline...;a source of strength and solace during life's storms.''', 'FRIEND FACT'),
('''True friends are like family...;they stand by us, love us unconditionally, and share in our joys and sorrows.''', 'FRIEND FACT'),
('''Friendship is a symphony...;harmonizing different personalities and creating beautiful melodies of love and support.''', 'FRIEND FACT'),
('''Friendship is a celebration...;marking the moments of laughter, growth, and shared memories.''', 'FRIEND FACT'),
('''True friends are like rare gems...;their presence is precious, and they add sparkle to our lives.''', 'FRIEND FACT'),
('''Friendship is a language of the heart...;spoken through gestures, kindness, and understanding.''', 'FRIEND FACT'),
('''A boy's kindness has the power to touch hearts...;he shows empathy and compassion towards others.''', 'BOY FACT'),
('''A boy's determination fuels his success...;he sets goals and perseveres to achieve them.''', 'BOY FACT'),
('''A boy's friendship is a source of joy...;he creates strong bonds and shares memorable moments with his friends.''', 'BOY FACT'),
('''A boy's imagination knows no limits...;he can turn anything into an adventure with his creative mind.''', 'BOY FACT'),
('''A boy's support is unwavering...;he stands by his loved ones in their times of need.''', 'BOY FACT'),
('''A girl's smile lights up the room...;her happiness is contagious and brings joy to those around her.''', 'GIRL FACT'),
('''A girl's courage empowers her...;she fearlessly takes on challenges and overcomes obstacles.''', 'GIRL FACT'),
('''A girl's friendship is a precious gift...;she is a loyal and supportive companion to her friends.''', 'GIRL FACT'),
('''A girl's intuition guides her...;she trusts her instincts and makes wise decisions.''', 'GIRL FACT'),
('''A girl's warmth radiates...;she creates a welcoming and nurturing atmosphere for those around her.''', 'GIRL FACT'),
('''True friends are like anchors...;they provide stability and keep us grounded during turbulent times.''', 'FRIEND FACT'),
('''Friendship is a source of laughter and joy...;we share funny moments and create lifelong memories together.''', 'FRIEND FACT'),
('''Friendship is built on trust and honesty...;we confide in each other and speak our hearts without judgment.''', 'FRIEND FACT'),
('''Friendship is a support system...;we offer each other strength, encouragement, and a shoulder to lean on.''', 'FRIEND FACT'),
('''True friends celebrate each other's successes...;they are genuinely happy for each other's achievements.''', 'FRIEND FACT'),
('''Friendship is a bond that transcends distance...;we stay connected even when miles apart.''', 'FRIEND FACT'),
('''Friendship is like a cozy blanket...;it wraps us in warmth and makes us feel safe and loved.''', 'FRIEND FACT'),
('''True friends understand our silence...;they can sense our emotions even when we don't say a word.''', 'FRIEND FACT'),
('''Friendship is a source of inspiration...;we motivate and inspire each other to be the best versions of ourselves.''', 'FRIEND FACT'),
('''Friendship is a lifeline in tough times...;we offer support and encouragement during challenging moments.''', 'FRIEND FACT'),
('''True friends accept us as we are...;they love us unconditionally, flaws and all.''', 'FRIEND FACT'),
('''Friendship is a constant presence...;we know we can count on each other, no matter what.''', 'FRIEND FACT'),
('''Friendship is a beautiful dance...;we move together in harmony, understanding each other's steps.''', 'FRIEND FACT'),
('''True friends are like soulmates...;they connect with us on a deeper level and understand our innermost thoughts.''', 'FRIEND FACT'),
('''Friendship is a bond that withstands time...;we cherish lifelong friendships that endure through the years.''', 'FRIEND FACT'),
('''Friendship is a source of laughter and joy...;we share funny moments and create lifelong memories together.''', 'FRIEND FACT'),
('''A boy's enthusiasm is contagious...;his energy and passion inspire those around him.''', 'BOY FACT'),
('''A boy's compassion knows no bounds...;he empathizes with others and lends a helping hand.''', 'BOY FACT'),
('''A boy's determination drives him to succeed...;he sets goals and works hard to achieve them.''', 'BOY FACT'),
('''A boy's friendship is a treasure...;he values his friends and creates lasting bonds with them.''', 'BOY FACT'),
('''A boy's creativity knows no limits...;he can transform ordinary things into something extraordinary.''', 'BOY FACT'),
('''A girl's kindness brightens the world...;she spreads love and makes a positive impact on those around her.''', 'GIRL FACT'),
('''A girl's intelligence shines through...;she possesses a sharp mind and is eager to learn and grow.''', 'GIRL FACT'),
('''A girl's friendship is a source of strength...;she uplifts and supports her friends in times of need.''', 'GIRL FACT'),
('''A girl's empathy touches hearts...;she understands the emotions of others and offers comfort and understanding.''', 'GIRL FACT'),
('''A girl's determination propels her forward...;she overcomes challenges and achieves her dreams.''', 'GIRL FACT'),
('''True friends are like rays of sunshine...;they bring warmth, happiness, and light into our lives.''', 'FRIEND FACT'),
('''Friendship is a shelter in the storm...;we find solace and support in the embrace of true friends.''', 'FRIEND FACT'),
('''Friendship is a melody of laughter and joy...;we create beautiful memories through shared laughter and fun moments.''', 'FRIEND FACT'),
('''Friendship is a symphony of trust...;we trust each other wholeheartedly and have faith in our friendship.''', 'FRIEND FACT'),
('''True friends are like anchors in a storm...;they provide stability and support during turbulent times.''', 'FRIEND FACT'),
('''Friendship is a garden of love...;we nurture and cultivate our friendships with care and affection.''', 'FRIEND FACT'),
('''Friendship is a bond that knows no boundaries...;we connect and understand each other regardless of differences.''', 'FRIEND FACT'),
('''True friends are like guiding stars...;they lead us in the right direction and help us find our way.''', 'FRIEND FACT'),
('''Friendship is a tapestry of memories...;we weave together moments of laughter, tears, and shared experiences.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of understanding...;we can be our true selves without fear of judgment or pretense.''', 'FRIEND FACT'),
('''True friends are like rare gems...;they are precious, valuable, and hard to find.''', 'FRIEND FACT'),
('''Friendship is a bridge of support...;we lean on each other during tough times and offer strength and encouragement.''', 'FRIEND FACT'),
('''Friendship is a celebration of diversity...;we embrace and appreciate each other's unique qualities and differences.''', 'FRIEND FACT'),
('''True friends are like puzzle pieces...;they fit together perfectly and complement each other's strengths and weaknesses.''', 'FRIEND FACT'),
('''Friendship is a bond that grows with time...;we cherish and nurture our friendships throughout the years.''', 'FRIEND FACT'),
('''Friendship is a source of inspiration...;we inspire each other to be the best versions of ourselves.''', 'FRIEND FACT'),
('''A boy's determination fuels his dreams...;he relentlessly pursues his passions and strives for success.''', 'BOY FACT'),
('''A boy's resilience is remarkable...;he bounces back from setbacks and never gives up.''', 'BOY FACT'),
('''A boy's generosity knows no bounds...;he selflessly helps others and gives without expecting anything in return.''', 'BOY FACT'),
('''A boy's leadership shines through...;he inspires others with his vision and guides them towards greatness.''', 'BOY FACT'),
('''A boy's friendship is a pillar of support...;he is a loyal companion and always has his friends' backs.''', 'BOY FACT'),
('''A girl's confidence is radiant...;she believes in herself and embraces her unique qualities with pride.''', 'GIRL FACT'),
('''A girl's resilience is awe-inspiring...;she overcomes challenges with grace and emerges stronger than ever.''', 'GIRL FACT'),
('''A girl's empathy touches souls...;she understands the emotions of others and offers comfort and support.''', 'GIRL FACT'),
('''A girl's ambition knows no bounds...;she sets ambitious goals and works tirelessly to achieve them.''', 'GIRL FACT'),
('''A girl's friendship is a treasure...;she is a loyal and trustworthy friend, always there to lend a listening ear.''', 'GIRL FACT'),
('''True friends are like guardian angels...;they protect us from harm and guide us towards the right path.''', 'FRIEND FACT'),
('''Friendship is a symphony of laughter...;we share joyous moments and create beautiful memories together.''', 'FRIEND FACT'),
('''Friendship is a refuge in times of sorrow...;we find solace and comfort in the embrace of true friends.''', 'FRIEND FACT'),
('''Friendship is a tapestry of trust...;we confide in each other and trust that our secrets will be kept safe.''', 'FRIEND FACT'),
('''True friends are like beacons of light...;they guide us through darkness and bring warmth to our lives.''', 'FRIEND FACT'),
('''Friendship is a bond that transcends differences...;we celebrate diversity and appreciate each other's uniqueness.''', 'FRIEND FACT'),
('''Friendship is a source of inspiration...;we motivate and empower each other to reach for our dreams.''', 'FRIEND FACT'),
('''True friends are like puzzle pieces...;each one is unique, but together they create a beautiful picture.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of acceptance...;we embrace each other for who we truly are, without judgment.''', 'FRIEND FACT'),
('''Friendship is a garden of growth...;we encourage and support each other's personal and emotional development.''', 'FRIEND FACT'),
('''True friends are like anchors in a storm...;they provide stability and support during challenging times.''', 'FRIEND FACT'),
('''Friendship is a symphony of laughter and tears...;we share both the joyous and challenging moments of life together.''', 'FRIEND FACT'),
('''Friendship is a treasure chest of memories...;filled with moments of laughter, adventures, and shared experiences.''', 'FRIEND FACT'),
('''True friends are like guiding stars...;they lead us in the right direction and illuminate our path.''', 'FRIEND FACT'),
('''Friendship is a source of comfort...;we find solace and reassurance in the presence of true friends.''', 'FRIEND FACT'),
('''A boy's laughter brings sunshine to the room...;his infectious giggles brighten up everyone's day.''', 'BOY FACT'),
('''A boy's kindness knows no limits...;he goes out of his way to help others and spread positivity.''', 'BOY FACT'),
('''A boy's curiosity fuels his endless exploration...;he constantly seeks new knowledge and experiences.''', 'BOY FACT'),
('''A boy's resilience empowers him to overcome challenges...;he never gives up and learns from every setback.''', 'BOY FACT'),
('''A boy's creativity knows no boundaries...;he has a knack for thinking outside the box and finding innovative solutions.''', 'BOY FACT'),
('''A girl's smile lights up the room...;her radiant grin brings joy to those around her.''', 'GIRL FACT'),
('''A girl's strength is undeniable...;she faces adversity with courage and determination.''', 'GIRL FACT'),
('''A girl's compassion touches hearts...;she has a natural ability to understand and support others in need.''', 'GIRL FACT'),
('''A girl's confidence is inspiring...;she believes in herself and encourages others to embrace their uniqueness.''', 'GIRL FACT'),
('''A girl's friendship is a precious gift...;she treasures her friends and cherishes the bond they share.''', 'GIRL FACT'),
('''True friends are like stars that never fade...;their presence shines brightly in our lives, guiding us through darkness.''', 'FRIEND FACT'),
('''Friendship is a dance of trust and understanding...;we move in harmony, supporting and uplifting each other.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of authenticity...;we can be our true selves without fear of judgment or pretense.''', 'FRIEND FACT'),
('''Friendship is a symphony of laughter and tears...;we share moments of joy and comfort each other in times of sadness.''', 'FRIEND FACT'),
('''True friends are like anchors in the storm...;they provide stability and support during life's turbulent times.''', 'FRIEND FACT'),
('''Friendship is a garden of memories...;we sow seeds of laughter, adventure, and unforgettable experiences.''', 'FRIEND FACT'),
('''Friendship is a tapestry of shared dreams...;we inspire and encourage each other to reach for the stars.''', 'FRIEND FACT'),
('''Friendship is a celebration of uniqueness...;we embrace our differences and learn from one another's perspectives.''', 'FRIEND FACT'),
('''True friends are like puzzle pieces...;each one fits perfectly, complementing and completing the bigger picture.''', 'FRIEND FACT'),
('''Friendship is a source of strength...;we lean on each other during challenging times and find solace in our connection.''', 'FRIEND FACT'),
('''Friendship is a symphony of support...;we lift each other up, cheering on our victories and offering comfort in defeat.''', 'FRIEND FACT'),
('''Friendship is a treasure trove of laughter...;we create joyful memories that will be cherished forever.''', 'FRIEND FACT'),
('''A boy's curiosity fuels his thirst for knowledge...;he is constantly seeking to expand his understanding of the world.''', 'BOY FACT'),
('''A boy's determination drives him to achieve greatness...;he sets goals and works tirelessly to turn them into reality.''', 'BOY FACT'),
('''A boy's empathy touches the hearts of others...;he has a deep understanding of people's emotions and offers support and compassion.''', 'BOY FACT'),
('''A boy's resilience allows him to bounce back from setbacks...;he learns from his experiences and grows stronger through adversity.''', 'BOY FACT'),
('''A boy's kindness makes the world a better place...;he goes out of his way to help others and spread positivity.''', 'BOY FACT'),
('''A girl's laughter is infectious...;her giggles fill the air and bring joy to everyone around her.''', 'GIRL FACT'),
('''A girl's strength is admirable...;she faces challenges head-on and perseveres with grace and determination.''', 'GIRL FACT'),
('''A girl's empathy knows no bounds...;she understands the emotions of others and offers a comforting presence.''', 'GIRL FACT'),
('''A girl's resilience shines in difficult times...;she rises above adversity and emerges stronger on the other side.''', 'GIRL FACT'),
('''A girl's confidence radiates...;she believes in herself and inspires others to embrace their own unique qualities.''', 'GIRL FACT'),
('''True friends are like stars in the night sky...;they provide guidance and shine brightly in our darkest moments.''', 'FRIEND FACT'),
('''Friendship is a bond that withstands the test of time...;it grows stronger and deeper with each passing year.''', 'FRIEND FACT'),
('''Friendship is a tapestry of trust and loyalty...;we can rely on each other and know that our secrets are safe.''', 'FRIEND FACT'),
('''Friendship is a symphony of shared experiences...;we create beautiful melodies of laughter, joy, and support.''', 'FRIEND FACT'),
('''True friends are like a second family...;they provide love, support, and a sense of belonging in our lives.''', 'FRIEND FACT'),
('''Friendship is a garden of laughter...;we nurture it with jokes, inside jokes, and laughter that bonds us together.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of understanding...;we listen, empathize, and support each other without judgment.''', 'FRIEND FACT'),
('''Friendship is a symphony of acceptance...;we embrace each other's quirks, flaws, and unique personalities.''', 'FRIEND FACT'),
('''True friends are like anchors...;they provide stability and support during life's storms and challenges.''', 'FRIEND FACT'),
('''Friendship is a mosaic of memories...;we piece together moments of joy, laughter, and shared adventures.''', 'FRIEND FACT'),
('''Friendship is a source of inspiration...;we motivate and empower each other to reach for our dreams and aspirations.''', 'FRIEND FACT'),
('''Friendship is a celebration of authenticity...;we encourage and celebrate each other's true selves without judgment.''', 'FRIEND FACT'),
('''True friends are like guardian angels...;they watch over us, protect us, and offer guidance when we need it the most.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of trust...;we confide in each other and know that our secrets are safe in each other's hands.''', 'FRIEND FACT'),
('''True friends are like guardian angels...;they protect us, guide us, and provide a shoulder to lean on.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of acceptance...;we embrace and celebrate each other's flaws and imperfections.''', 'FRIEND FACT'),
('''Friendship is a garden of growth...;we nourish and encourage each other to blossom into our best selves.''', 'FRIEND FACT'),
('''A boy's laughter is contagious...;it spreads joy and brings smiles to those around him.''', 'BOY FACT'),
('''A boy's courage knows no bounds...;he fearlessly embraces challenges and stands up for what he believes in.''', 'BOY FACT'),
('''A boy's imagination knows no limits...;he can turn the simplest objects into magical adventures.''', 'BOY FACT'),
('''A boy's loyalty is unwavering...;he stands by his friends through thick and thin.''', 'BOY FACT'),
('''A boy's enthusiasm is infectious...;he brings energy and excitement to every situation.''', 'BOY FACT'),
('''A girl's laughter is music to the ears...;her joyous giggles fill the air with happiness.''', 'GIRL FACT'),
('''A girl's kindness shines through...;she has a compassionate heart and is always there to lend a helping hand.''', 'GIRL FACT'),
('''A girl's resilience is remarkable...;she bounces back from adversity and never loses her spirit.''', 'GIRL FACT'),
('''A girl's creativity knows no bounds...;she has a vivid imagination and brings beauty to the world through her art.''', 'GIRL FACT'),
('''A girl's friendship is a treasure...;she values her friends and cherishes the bond they share.''', 'GIRL FACT'),
('''True friends are like stars in the night sky...;they illuminate our path and bring comfort to our souls.''', 'FRIEND FACT'),
('''Friendship is a garden of laughter and love...;we nurture it with kindness, understanding, and shared memories.''', 'FRIEND FACT'),
('''Friendship is a tapestry of trust and honesty...;we confide in each other and know our secrets are safe.''', 'FRIEND FACT'),
('''Friendship is a symphony of support and encouragement...;we lift each other up and believe in each other's dreams.''', 'FRIEND FACT'),
('''True friends are like a warm embrace...;they provide comfort and solace in times of need.''', 'FRIEND FACT'),
('''Friendship is a sanctuary of acceptance and understanding...;we embrace each other's flaws and celebrate our uniqueness.''', 'FRIEND FACT'),
('''Friendship is a tapestry of shared adventures...;we create unforgettable memories that will last a lifetime.''', 'FRIEND FACT'),
('''Friendship is a source of inspiration and growth...;we motivate and challenge each other to become the best versions of ourselves.''', 'FRIEND FACT'),
('''True friends are like pillars of strength...;they provide support and stability in our lives.''', 'FRIEND FACT'),
('''Friendship is a symphony of laughter and tears...;we share both joyous and challenging moments with open hearts.''', 'FRIEND FACT'),
('''Friendship is a treasure chest of memories...;we fill it with moments of laughter, love, and shared experiences.''', 'FRIEND FACT'),
('''True friends are like guiding stars...;they light up our lives and guide us through the ups and downs.''', 'FRIEND FACT'),
('''Friendship is a source of comfort and understanding...;we find solace in the presence of true friends.''', 'FRIEND FACT'),
('''Friendship is a tapestry of trust and loyalty...;we stand by each other through thick and thin.''', 'FRIEND FACT'),
('''Friendship is a garden of growth and support...;we nurture each other's dreams and help them blossom.''', 'FRIEND FACT'),
]
for fact in quotes:
    quote_text, quote_heading = fact

    insert_query = "INSERT INTO Quotes (QuoteText, QuoteHeading) VALUES (%s, %s)"
    values = (quote_text,quote_heading)

    try:

        cursor.execute(insert_query, values)

    except Exception as e: 
        print(e)
    conn.commit()


# Close cursor and connection
cursor.close()
conn.close()