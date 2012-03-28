# coding=utf8

# 从官网http://www.justiceharvard.org/取到的Lecture标题
lecture_titles = (
            'Lecture 1 - The Morality of Murder',
            'Lecture 2 - How Much is a Life Worth?',
            'Lecture 3 - Redistributive Taxation and Progressive Taxation - Freedom to Choose',
            'Lecture 4 - Natural Rights and Giving Them Up',
            'Lecture 5 - Avoiding the Draft and Avoiding Parenthood',
            'Lecture 6 - Motives and Morality',
            'Lecture 7 - Lying and Principles',
            "Lecture 8 - What's Fair and Deserved?",
            'Lecture 9 - Affirmative Action and Purpose',
            'Lecture 10 - The Good Citizen and the Freedom to Choose',
            'Lecture 11 - Oblig:ations and Loyalties',
            'Lecture 12 - Same Sex Marriage',
        )

# 从http://academicearth.org/courses/justice-whats-the-right-thing-to-doing
# 取到的Lecture简介，每个Part中间加了空行 </br></br>
lecture_descriptions = (
"""Part 1 - The Moral Side of Murder: If you had to choose between (1) killing one person to save the lives of five others and (2) doing nothing, even though you knew that five people would die right before your eyes if you did nothing--what would you do? What would be the right thing to do? That's the hypothetical scenario Professor Michael Sandel uses to launch his course on moral reasoning.</br>

</br>Part 2 - The Case for Cannibalism: Sandel introduces the principles of utilitarian philosopher, Jeremy Bentham, with a famous nineteenth century law case involving a shipwrecked crew of four. After nineteen days lost at sea, the captain decides to kill the cabin boy, the weakest amongst them, so they can feed on his blood and body to survive.""",

"""Part 1 - Putting a Price Tag on Life: Today, companies and governments often use Jeremy Bentham's utilitarian logic under the name of "cost-benefit analysis." Sandel presents some contemporary cases in which cost-benefit analysis was used to put a dollar value on human life. The cases give rise to several objections to the utilitarian logic of seeking "the greatest good for the greatest number." Should we always give more weight to the happiness of a majority, even if the majority is cruel or ignoble? Is it possible to sum up and compare all values using a common measure like money?</br>

</br>Part 2 - How to Measure Pleasure: Sandel introduces J.S. Mill, a utilitarian philosopher who attempts to defend utilitarianism against the objections raised by critics of the doctrine. Mill argues that seeking "the greatest good for the greatest number" is compatible with protecting individual rights, and that utilitarianism can make room for a distinction between higher and lower pleasures. Mill's idea is that the higher pleasure is always the pleasure preferred by a well-informed majority. Sandel tests this theory by playing video clips from three very different forms of entertainment: Shakespeare's Hamlet, the reality show Fear Factor, and The Simpsons. Students debate which experience provides the higher pleasure, and whether Mill's defense of utilitarianism is successful.
""",

"""Part 1 - Free to Choose: With humorous references to Bill Gates and Michael Jordan, Sandel introduces the libertarian notion that redistributive taxation--taxing the rich to give to the poor--is akin to forced labor. </br>

</br>Part 2 - Who Owns Me?: Students first discuss the arguments behind redistributive taxation. If you live in a society that has a system of progressive taxation, aren't you obligated to pay your taxes? Don't many rich people often acquire their wealth through sheer luck or family fortune? A group of students dubbed "Team Libertarian" volunteers to defend the libertarian philosophy against these objections.
""",

"""Part 1 - This Land is My Land: The philosopher John Locke believes that individuals have certain rights--to life, liberty, and property--which were given to us as human beings in the "the state of nature," a time before government and laws were created. According to Locke, our natural rights are governed by the law of nature, known by reason, which says that we can neither give them up nor take them away from anyone else.</br>

</br>Part 2 - Consenting Adults: If we all have unalienable rights to life, liberty, and property, how can a government enforce tax laws passed by the representatives of a mere majority? Doesn't that amount to taking some people's property without their consent? Locke's response is that we give our "tacit consent" to obey the tax laws passed by a majority when we choose to live in a society.
""",

"""Part 1 - Hired Guns?: During the Civil War, men drafted into war had the option of hiring substitutes to fight in their place. Many students say they find that policy unjust, arguing that it is unfair to allow the affluent to avoid serving and risking their lives by paying less privileged citizens to fight in their place. This leads to a classroom debate about war and conscription. Is today's voluntary army open to the same objection?</br>

</br>Part 2 - For Sale: Motherhood: Professor Sandel examines the principle of free-market exchange as it relates to reproductive rights. Sandel begins with a humorous discussion of the business of egg and sperm donation. He then describes the case of "Baby M"--a famous legal battle that raised the unsettling question, "Who owns a baby?" Students debate the nature of informed consent, the morality of selling a human life, and the meaning of maternal rights.
""",

"""Part 1 - Mind Your Motive: Professor Sandel introduces Immanuel Kant, a challenging but influential philosopher. Kant rejects utilitarianism. He argues that each of us has certain fundamental duties and rights that take precedence over maximizing utility. Kant rejects the notion that morality is about calculating consequences. When we act out of duty--doing something simply because it is right--only then do our actions have moral worth.</br>

</br>Part 2 - Supreme Principal of Morality: Immanuel Kant says that insofar as our actions have moral worth, what confers moral worth is our capacity to rise above self-interest and inclination and to act out of duty. Sandel tells the true story of a thirteen-year-old boy who won a spelling bee contest, but then admitted to the judges that he had, in fact, misspelled the final word.
""",

"""Part 1 - A Lesson in Lying: Immanuel Kant believed that telling a lie, even a white lie, is a violation of one's own dignity. Professor Sandel asks students to test Kant's theory with this hypothetical case: if your friend were hiding inside your home, and a person intent on killing your friend came to your door and asked you where he was, would it be wrong to tell a lie? This leads to a video clip of one of the most famous, recent examples of dodging the truth: President Clinton talking about his relationship with Monica Lewinsky.</br>

</br>Part 2 - A Deal is a Deal: Sandel introduces the modern philosopher, John Rawls, who argues that a fair set of principles would be those principles we would all agree to if we had to choose rules for our society and no one had any unfair bargaining power.
""",

"""Part 1 - What's a Fair Start?: Rawls argues that even meritocracy--a distributive system that rewards effort--doesn't go far enough in leveling the playing field because those who are naturally gifted will always get ahead. Furthermore, says Rawls, the naturally gifted can't claim much credit because their success often depends on factors as arbitrary as birth order. Sandel makes Rawls's point when he asks the students who were first born in their family to raise their hands.</br>

</br>Part 2 - What Do We Deserve?: Sandel discusses the fairness of pay differentials in modern society. He compares the salary of former Supreme Court Justice Sandra Day O'Connor ($200,000) with the salary of television's Judge Judy ($25 million). Sandel asks, is this fair? According to John Rawls, it is not.
""",

"""Part 1 - Arguing Affirmative Action: Sandel describes the 1996 court case of a white woman named Cheryl Hopwood who was denied admission to a Texas law school, even though she had higher grades and test scores than some of the minority applicants who were admitted. Hopwood took her case to court, arguing the school's affirmative action program violated her rights. Students discuss the pros and cons of affirmative action.</br>

</br>Part 2 - What's the Purpose?: Aristotle disagrees with Rawls and Kant. When considering matters of distribution, Aristotle argues one must consider the goal, the end, the purpose of what is being distributed. Justice is a matter of fitting a person's virtues with an appropriate role. And the highest political offices should go to those with the best judgment and the greatest civic virtue.
""",

"""Part 1 - The Good Citizen: Aristotle believes the purpose of politics is to promote and cultivate the virtue of its citizens. The telos or goal of the state and political community is the "good life". And those citizens who contribute most to the purpose of the community are the ones who should be most rewarded. But how do we know the purpose of a community or a practice? Aristotle's theory of justice leads to a contemporary debate about golf. Sandel describes the case of Casey Martin, a disabled golfer, who sued the PGA after it declined his request to use a golf cart on the PGA Tour. The case leads to a debate about the purpose of golf and whether a player's ability to "walk the course" is essential to the game. </br>

</br>Part 2 - Freedom vs. Fit: How does Aristotle address the issue of individual rights and the freedom to choose? If our place in society is determined by where we best fit, doesn't that eliminate personal choice? What if I am best suited to do one kind of work, but I want to do another? In this lecture, Sandel addresses one of the most glaring objections to Aristotle's views on freedom--his defense of slavery as a fitting social role for certain human beings. Students discuss other objections to Aristotle's theories and debate whether his philosophy overly restricts the freedom of individuals.
""",

""""Part 1 - The Claims of Community: Communitarians argue that, in addition to voluntary and universal duties, we also have obligations of membership, solidarity, and loyalty. These obligations are not necessarily based on consent. We inherit our past, and our identities, from our family, city, or country. But what happens if our obligations to our family or community come into conflict with our universal obligations to humanity?</br>

</br>Part 2 - Where Our Loyalties Lie: Do we owe more to our fellow citizens that to citizens of other countries? Is patriotism a virtue, or a prejudice for one's own kind? If our identities are defined by the particular communities we inhabit, what becomes of universal human rights?
""",

"""Part 1 -Debating Same Sex Marraige: If principles of justice depend on the moral or intrinsic worth of the ends that rights serve, how should we deal with the fact that people hold different ideas and conceptions of what is good? Students address this question in a heated debate about whether same-sex marriage should be legal. Can we settle the matter without discussing the moral permissibility of homosexuality or the purpose of marriage?</br>

</br>Part 2 - The Good Life: Sandel believes government can't be neutral on difficult moral questions, such as same-sex marriage and abortion, and asks why we shouldn't deliberate all issues--including economic and civic concerns--with that same moral and spiritual aspiration. In his final lecture, Professor Michael Sandel eloquently makes the case for a new politics of the common good. Engaging, rather than avoiding, the moral convictions of our fellow citizens may be the best way of seeking a just society.
""",
        )


# 输出的html文件及html内容
html_file = open("Justice-What's the Right Thing to Do.html", 'w')
html_file.write("""
<html xmlns="http://www.w3.org/1999/xhtml" lang="utf8">
    <head><title>Justice: What's the Right Thing to Do?</title></head>
    <body>
        <center><h3>Justice: What's the Right Thing to Do?</h3></center>
"""
)

# 以html链接的形式加上目录
contents_table = '<h4>--Table of Contents:</h4>'
for i in range(1, 13):
    contents_table += '''<h5><a href="#Lecture%s">%s</a></h5>''' % (i, lecture_titles[i-1])
html_file.write(contents_table)

# 遍历本地12个 .srt 字幕文件
for i in range(1, 13):
    file_name = 'Lecture%s.srt' % i
    srt_file = open(file_name, 'r')
    whole_file = srt_file.read()
    srt_file.close()

    all_lines = whole_file.split('\r\n')
    contents = [ ] # 一个Lecture的完整字幕
    sentence = '' # 字幕的每行可能不是完整句子的结束

    for line in all_lines:
        if not ('-->' in line or (line is '\r\n') or len(line)<=3):
            if line.endswith(('.', '?', '!', ':')):
                sentence = '''<p>%s%s</p>''' % (sentence, line)
                contents.append(sentence) # 完整一个句子
                sentence = ''
            else:
                sentence += line + ' ' # 需判断下一行直到句子完整

    txt_contents = '\r\n\r\n'.join(contents)
    #print txt_contents
    txt_file = open('%s.txt' % file_name, 'w') # 每个Lecture输出为一个txt文件
    txt_file.write(txt_contents)
    txt_file.close()

    html_contents = ''.join(contents)
    html_file.write('</br></br></br>')
    html_file.write('''<center><h3 id="Lecture%s">%s</h3></center>''' % (i, lecture_titles[i-1]))
    html_file.write(('''<h5>--Lecture Description:</h5>%s</br></br>''' % lecture_descriptions[i-1]))
    html_file.write(html_contents)


html = '''
    </body>
</html>'''
html_file.write(html)
html_file.close()

