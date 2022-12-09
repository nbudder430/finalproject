from tkinter import *
import csv


class GUI:
    def __init__(self, window) -> None:
        """
        Function that creates the starting window
        :param window: The starting window
        """
        self.window = window
        window.configure(bg= "WHITE")
        self.frame_main = Frame(self.window)
        self.label_title = Label(self.frame_main, text="The D&D Balance Test", bg= "Black", fg="WHITE")
        self.label_title.pack(padx=0, side='left')
        self.frame_main.pack(pady=40)
        self.label_title.config(font=('Times', 40, "underline", "bold"))

        self.frame_info = Frame(self.window)
        self.label_info = Label(self.frame_info, text="\n Dungeons and dragons has been around for years now, \n"
                                                      " but it has seen a massive jump in players with new \n"
                                                      " representation in all sorts of media. That means that \n"
                                                      " there are people who are playing for the first time, \n"
                                                      " and that can be extremely daunting. One big issue that \n"
                                                      " both DMs and players run into is balancing a party. \n"
                                                      " If there are too many magic users, then the party \n"
                                                      " might not have enough physical strength. However, if \n"
                                                      " there is too much up-close representation, your range \n"
                                                      " is weakened and you don't have the aid of magic. This \n"
                                                      " tool will take your party and determine whether or not \n"
                                                      " the team is balanced, and will suggest a change or two. \n"
                                                      "\n\n Have fun! \n")
        self.label_info.pack(padx=0, side='left')
        self.frame_info.pack(pady=8)
        self.label_info.config(font=('Times', 14, "italic"), bg= "BLACK", fg= "WHITE")

        self.frame_mainButtons = Frame(self.window)
        self.button_extraInfo = Button(self.frame_mainButtons, text='FURTHER DETAILS', command=self.openinfo,height= 2,
                                       width=30, bg="BLACK", fg="WHITE")
        self.button_begin = Button(self.frame_mainButtons, text='START BALANCING!', command=self.clicked_start, height=2,
                                       width=30, bg="BLACK", fg="WHITE")
        self.button_extraInfo.pack(side = "left")
        self.button_begin.pack(side = "left")
        self.frame_mainButtons.pack(pady=50)

    def openinfo(self) -> None:
        """
        Function that creates a window with extra information
        :return: None
        """
        extrainfo = Tk()
        extrainfo.title("Extra Information")
        extrainfo.geometry("600x700")
        extrainfo.resizable(False, False)
        self.extrainfo = extrainfo
        extrainfo.configure(bg="WHITE")
        self.frame_exinfo = Frame(self.extrainfo)
        self.label_exinfo = Label(self.frame_exinfo, text="Extra Info", bg="Black", fg="WHITE")
        self.label_exinfo.pack(padx=0, side='left')
        self.frame_exinfo.pack(pady=40)
        self.label_exinfo.config(font=('Times', 40, "underline", "bold"))

        self.frame_history = Frame(self.extrainfo)
        self.label_history = Label(self.frame_history, text="\n My D&D History \n\n"
                                                      " I have been playing D&D for about 4 years now. \n"
                                                      " I've done everything from playing as a character to being \n"
                                                      " a DM to even just watching the game being played. I decided \n"
                                                      " to create this tool because I started a campaign a year and \n"
                                                      " a half ago. I had never been the Dungeon Master before \n"
                                                      " so the original team that they made was terribly unbalanced. \n"
                                                      " That's why I created this system to get a functional team. \n")
        self.label_history.pack(padx=0, side='left')
        self.frame_history.pack(pady=2)
        self.label_history.config(font=('Times', 14, "italic"), bg="BLACK", fg="WHITE")

        self.frame_explanation = Frame(self.extrainfo)
        self.label_explanation = Label(self.frame_explanation, text="\n System Explanation \n\n"
                                                                    " Each class is given a point value determined \n"
                                                                    " by its magic usage. The scale gives 2 points \n"
                                                                    " to major magical users, 1 point to partial \n"
                                                                    " magic users, no points to balanced classes, \n"
                                                                    " -1 point to partial martial classes, and \n"
                                                                    " -2 points to major martial classes. If the \n"
                                                                    " party's point total is above 3 or below -3, \n"
                                                                    " then the party is outside of the optimal \n"
                                                                    " party balance range, and Adjustments are needed."
                                                                    "\n")
        self.label_explanation.pack(padx=0, side='left')
        self.frame_explanation.pack(pady=8)
        self.label_explanation.config(font=('Times', 14, "italic"), bg="BLACK", fg="WHITE")

        extrainfo.mainloop()

    def clicked_start(self) -> None:
        """
        Function that creates the balancer window and its logic
        :return: None
        """
        balancer = Tk()
        balancer.title("The Party Balancer")
        balancer.geometry("600x700")
        balancer.resizable(False, False)
        self.balancer = balancer
        balancer.configure(bg="WHITE")
        self.frame_balancer = Frame(self.balancer)
        self.label_balancer = Label(self.frame_balancer, text="The Party Balancer", bg="Black", fg="WHITE")
        self.label_balancer.pack(padx=0, side='left')
        self.frame_balancer.pack(pady=20)
        self.label_balancer.config(font=('Times', 40, "underline", "bold"))

        self.frame_balanceinstructions = Frame(self.balancer)
        self.label_balanceinstructions = Label(self.frame_balanceinstructions, text=" Enter the number of characters \n"
                                                                                    " per class", bg="Black",
                                                                                    fg="WHITE")
        self.label_balanceinstructions.pack(padx=0, side='left')
        self.frame_balanceinstructions.pack(pady=4)
        self.label_balanceinstructions.config(font=('Times', 15, "italic"))

        self.frame_artificer = Frame(self.balancer)
        self.label_artificer = Label(self.frame_artificer, text='Artificer')
        self.entry_artificer = Entry(self.frame_artificer)
        self.entry_artificer.insert(END, "0")
        self.label_artificer.pack(padx=5, side='left')
        self.entry_artificer.pack(padx=5, side='left')
        self.frame_artificer.pack(pady=5)

        self.frame_barbarian = Frame(self.balancer)
        self.label_barbarian = Label(self.frame_barbarian, text='Barbarian')
        self.entry_barbarian = Entry(self.frame_barbarian)
        self.entry_barbarian.insert(END, "0")
        self.label_barbarian.pack(padx=5, side='left')
        self.entry_barbarian.pack(padx=5, side='left')
        self.frame_barbarian.pack(pady=5)

        self.frame_bard = Frame(self.balancer)
        self.label_bard = Label(self.frame_bard, text='Bard')
        self.entry_bard = Entry(self.frame_bard)
        self.entry_bard.insert(END, "0")
        self.label_bard.pack(padx=5, side='left')
        self.entry_bard.pack(padx=5, side='left')
        self.frame_bard.pack(pady=5)

        self.frame_cleric = Frame(self.balancer)
        self.label_cleric = Label(self.frame_cleric, text='Cleric')
        self.entry_cleric = Entry(self.frame_cleric)
        self.entry_cleric.insert(END, "0")
        self.label_cleric.pack(padx=5, side='left')
        self.entry_cleric.pack(padx=5, side='left')
        self.frame_cleric.pack(pady=5)

        self.frame_druid = Frame(self.balancer)
        self.label_druid = Label(self.frame_druid, text='Druid')
        self.entry_druid = Entry(self.frame_druid)
        self.entry_druid.insert(END, "0")
        self.label_druid.pack(padx=5, side='left')
        self.entry_druid.pack(padx=5, side='left')
        self.frame_druid.pack(pady=5)

        self.frame_fighter = Frame(self.balancer)
        self.label_fighter = Label(self.frame_fighter, text='Fighter')
        self.entry_fighter = Entry(self.frame_fighter)
        self.entry_fighter.insert(END, "0")
        self.label_fighter.pack(padx=5, side='left')
        self.entry_fighter.pack(padx=5, side='left')
        self.frame_fighter.pack(pady=5)

        self.frame_monk = Frame(self.balancer)
        self.label_monk = Label(self.frame_monk, text='Monk')
        self.entry_monk = Entry(self.frame_monk)
        self.entry_monk.insert(END, "0")
        self.label_monk.pack(padx=5, side='left')
        self.entry_monk.pack(padx=5, side='left')
        self.frame_monk.pack(pady=5)

        self.frame_paladin = Frame(self.balancer)
        self.label_paladin = Label(self.frame_paladin, text='Paladin')
        self.entry_paladin = Entry(self.frame_paladin)
        self.entry_paladin.insert(END, "0")
        self.label_paladin.pack(padx=5, side='left')
        self.entry_paladin.pack(padx=5, side='left')
        self.frame_paladin.pack(pady=5)

        self.frame_ranger = Frame(self.balancer)
        self.label_ranger = Label(self.frame_ranger, text='Ranger')
        self.entry_ranger = Entry(self.frame_ranger)
        self.entry_ranger.insert(END, "0")
        self.label_ranger.pack(padx=5, side='left')
        self.entry_ranger.pack(padx=5, side='left')
        self.frame_ranger.pack(pady=5)

        self.frame_rogue = Frame(self.balancer)
        self.label_rogue = Label(self.frame_rogue, text='Rogue')
        self.entry_rogue = Entry(self.frame_rogue)
        self.entry_rogue.insert(END, "0")
        self.label_rogue.pack(padx=5, side='left')
        self.entry_rogue.pack(padx=5, side='left')
        self.frame_rogue.pack(pady=5)

        self.frame_sorcerer = Frame(self.balancer)
        self.label_sorcerer = Label(self.frame_sorcerer, text='Sorcerer')
        self.entry_sorcerer = Entry(self.frame_sorcerer)
        self.entry_sorcerer.insert(END, "0")
        self.label_sorcerer.pack(padx=5, side='left')
        self.entry_sorcerer.pack(padx=5, side='left')
        self.frame_sorcerer.pack(pady=5)

        self.frame_warlock = Frame(self.balancer)
        self.label_warlock = Label(self.frame_warlock, text='Warlock')
        self.entry_warlock = Entry(self.frame_warlock)
        self.entry_warlock.insert(END, "0")
        self.label_warlock.pack(padx=5, side='left')
        self.entry_warlock.pack(padx=5, side='left')
        self.frame_warlock.pack(pady=5)

        self.frame_wizard = Frame(self.balancer)
        self.label_wizard = Label(self.frame_wizard, text='Wizard')
        self.entry_wizard = Entry(self.frame_wizard)
        self.entry_wizard.insert(END, "0")
        self.label_wizard.pack(padx=5, side='left')
        self.entry_wizard.pack(padx=5, side='left')
        self.frame_wizard.pack(pady=5)

        self.frame_balancerButtons = Frame(self.balancer)
        self.button_submit = Button(self.frame_balancerButtons, text='SUBMIT!', command=self.clicked_submit,height= 2,
                                       width=30, bg="BLACK", fg="WHITE")
        self.button_reset = Button(self.frame_balancerButtons, text='RESET', command=self.clicked_reset, height=2,
                                       width=30, bg="BLACK", fg="WHITE")
        self.button_submit.pack(side = "left")
        self.button_reset.pack(side = "left")
        self.frame_balancerButtons.pack(pady=20)

    def clicked_submit(self) -> None:
        """
        Function that takes results, calculates the party balance, and sends to new windows
        :return: None
        """
        artificer = int(self.entry_artificer.get()) * -1
        barbarian = int(self.entry_barbarian.get()) * -2
        bard = int(self.entry_bard.get())
        cleric = int(self.entry_cleric.get()) * 2
        druid = int(self.entry_druid.get()) * 2
        fighter = int(self.entry_fighter.get()) * -2
        monk = int(self.entry_fighter.get()) * -2
        paladin = 0
        ranger = int(self.entry_ranger.get()) * -1
        rogue = int(self.entry_rogue.get()) * -2
        sorcerer = int(self.entry_sorcerer.get()) * 2
        warlock = int(self.entry_warlock.get())
        wizard = int(self.entry_wizard.get()) * 2

        most_magic = cleric + druid + sorcerer + wizard
        some_magic = bard + warlock
        some_martial = ranger + artificer
        most_martial = barbarian + monk + fighter + rogue

        total = most_magic + some_magic + some_martial + most_martial

        if 3 >= total >= -3:
            balanced_party = Tk()
            balanced_party.title("Your Party Is Balanced")
            balanced_party.geometry("600x300")
            balanced_party.resizable(False, False)
            self.balanced_party = balanced_party
            balanced_party.configure(bg="WHITE")
            self.frame_balanced_party = Frame(self.balanced_party)
            self.label_balanced_party = Label(self.frame_balanced_party, text="Your Party Is Balanced!", bg="Black", fg="WHITE")
            self.label_balanced_party.pack(padx=0, side='left')
            self.frame_balanced_party.pack(pady=20)
            self.label_balanced_party.config(font=('Times', 40, "underline", "bold"))

            self.frame_bal_description = Frame(self.balanced_party)
            self.label_bal_description = Label(self.frame_bal_description, text="\n Your party is balanced! You have a good mix of both \n"
                                                          " magic users and heavy hitters that do their work up close \n"
                                                          " and personal. Good luck on your campaign! \n")
            self.label_bal_description.pack(padx=0, side='left')
            self.frame_bal_description.pack(pady=8)
            self.label_bal_description.config(font=('Times', 14, "italic"), bg="BLACK", fg="WHITE")
        elif total < -3:
            martial = Tk()
            martial.title("Your Party Is Too Martial")
            martial.geometry("600x300")
            martial.resizable(False, False)
            self.martial = martial
            martial.configure(bg="WHITE")
            self.frame_martial = Frame(self.martial)
            self.label_martial = Label(self.frame_martial, text="Your Party Is Too Martial!", bg="Black", fg="WHITE")
            self.label_martial.pack(padx=0, side='left')
            self.frame_martial.pack(pady=20)
            self.label_martial.config(font=('Times', 35, "underline", "bold"))

            self.frame_martial_description = Frame(self.martial)
            self.label_martial_description = Label(self.frame_martial_description,
                                                 text="\n Your party relies too heavily on martial combat! \n"
                                                      " Maybe change some of your martial users to more magic-oriented \n"
                                                      " classes like wizard or cleric and try again. Good luck! \n")
            self.label_martial_description.pack(padx=0, side='left')
            self.frame_martial_description.pack(pady=8)
            self.label_martial_description.config(font=('Times', 14, "italic"), bg="BLACK", fg="WHITE")
        elif total > 3:
            magic = Tk()
            magic.title("Your Party Is Too Magical")
            magic.geometry("600x300")
            magic.resizable(False, False)
            self.magic = magic
            magic.configure(bg="WHITE")
            self.frame_magic = Frame(self.magic)
            self.label_magic = Label(self.frame_magic, text="Your Party Is Too Magical!", bg="Black", fg="WHITE")
            self.label_magic.pack(padx=0, side='left')
            self.frame_magic.pack(pady=20)
            self.label_magic.config(font=('Times', 35, "underline", "bold"))

            self.frame_magic_description = Frame(self.magic)
            self.label_magic_description = Label(self.frame_magic_description, text="\n Your party relies too heavily on magic! \n"
                                                          " Maybe change some of your magic users to more martial-oriented \n"
                                                          " classes like barbarian or rogue and try again. Good luck! \n")
            self.label_magic_description.pack(padx=0, side='left')
            self.frame_magic_description.pack(pady=8)
            self.label_magic_description.config(font=('Times', 14, "italic"), bg="BLACK", fg="WHITE")
    def clicked_reset(self) -> None:
        """
        Function that resets all entry boxes to zero
        :return: None
        """
        self.entry_artificer.delete(0, END)
        self.entry_barbarian.delete(0, END)
        self.entry_bard.delete(0, END)
        self.entry_cleric.delete(0, END)
        self.entry_druid.delete(0, END)
        self.entry_fighter.delete(0, END)
        self.entry_monk.delete(0, END)
        self.entry_paladin.delete(0, END)
        self.entry_ranger.delete(0, END)
        self.entry_rogue.delete(0, END)
        self.entry_sorcerer.delete(0, END)
        self.entry_warlock.delete(0, END)
        self.entry_wizard.delete(0, END)
        self.entry_artificer.insert(END, "0")
        self.entry_barbarian.insert(END, "0")
        self.entry_bard.insert(END, "0")
        self.entry_cleric.insert(END, "0")
        self.entry_druid.insert(END, "0")
        self.entry_fighter.insert(END, "0")
        self.entry_monk.insert(END, "0")
        self.entry_paladin.insert(END, "0")
        self.entry_ranger.insert(END, "0")
        self.entry_rogue.insert(END, "0")
        self.entry_sorcerer.insert(END, "0")
        self.entry_warlock.insert(END, "0")
        self.entry_wizard.insert(END, "0")
