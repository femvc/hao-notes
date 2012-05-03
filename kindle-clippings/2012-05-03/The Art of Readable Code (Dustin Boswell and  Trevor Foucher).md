##The Art of Readable Code (Dustin Boswell and  Trevor Foucher)


- Highlight Loc. 766-67  | Added on Saturday, March 17, 2012, PM

The moral of the story is that making code “look pretty” often results in more than just surface improvements—it might help you structure your code better.



- Highlight Loc. 691-93  | Added on Saturday, March 17, 2012, PM

• Use consistent layout, with patterns the reader can get used to. • Make similar code look similar. • Group related lines of code into blocks.



- Highlight Loc. 845-46  | Added on Saturday, March 17, 2012, PM

We’ve worked on many projects where we felt like the team was using the “wrong” style, but we followed the project conventions because we knew that consistency is far more important.



- Highlight Loc. 847  | Added on Saturday, March 17, 2012, PM

Consistent style is more important than the “right” style.



- Highlight Loc. 874  | Added on Saturday, March 17, 2012, PM

Don’t comment on facts that can be derived quickly from the code itself.



- Highlight Loc. 1655-58  | Added on Sunday, March 18, 2012, AM

Specifically, we’ll cover three ways to reorganize your code: • Extract “unrelated subproblems” that aren’t related to the primary goal of your program. • Rearrange your code so it’s doing only one task at a time. • Describe your code in words first, and use this description to help guide you to a cleaner solution.



- Highlight Loc. 1661-62  | Added on Sunday, March 18, 2012, AM

Engineering is all about breaking down big problems into smaller ones and putting the solutions for those problems back together. Applying this principle to code makes it more robust and easier to read.



- Highlight Loc. 2116  | Added on Sunday, March 18, 2012, PM

The most readable code is no code at all.



- Highlight Loc. 2576-78  | Added on Monday, March 19, 2012, AM

It’s just as important for test code to be readable as it is for nontest code. Other coders will often look at the test code as unofficial documentation of how the real code works and should be used. So if the tests are easy to read, users will better understand how the real code behaves.



- Highlight Loc. 2794-96  | Added on Monday, March 19, 2012, AM

If you write your code knowing you’ll be writing a test for it later, a funny thing happens: you start designing your code so that it’s easy to test! Fortunately, coding this way also means that you create better code in general. Test-friendly designs often lead naturally to well-organized code, with separate parts to do separate things.



- Highlight Loc. 2938-41  | Added on Monday, March 19, 2012, PM

GETTING AN OUTSIDE PERSPECTIVE You may have noticed that there were already a couple cases where we ran things by our coworkers. Asking for an outside perspective is a great way to test if your code is “user-friendly.” Try to be open to their first impressions, because other people may come to the same conclusions. And those “other people” may include you in six 


