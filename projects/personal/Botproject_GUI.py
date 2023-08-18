from tkinter import *
import tkinter.messagebox

class BotGui:

	def __init__(self):

		self.username = None
		self.password = None
		self.room = None
		self.floor = None
		self.times_list = []
		self.ready = False



		self.button_dict = {}
		self.times = ['12:00am', '1:00am', '2:00am', '3:00am', '4:00am', '5:00am', '6:00am', '7:00am', '8:00am', '9:00am', '10:00am', '11:00am', '12:00pm', '1:00pm', '2:00pm', '3:00pm', '4:00pm', '5:00pm', '6:00pm', '7:00pm', '8:00pm', '9:00pm', '10:00pm', '11:00pm' ]
		rooms4 = {'Egret':'Room 409', 'Goldeneye':'Room 411', 'Quail':'Room 431', 'Tern':'Room 433', 'Warbler':'Room 435'}
		rooms5 = {'Hemlock':'Room 503', 'Ironwood':'Room 505', 'Juniper':'Room 509', 'Laurel':'Room 511', 'Mesquite':'Room 513', 'Palm':'Room 517', 'Redwood':'Room 519', 'Tamarack':'Room 521'}


		self.root = Tk()
		self.root.geometry('1300x500')

		button_frame = Frame(self.root)
		button_frame.grid()		

		floor_4 = Button(button_frame, text = 'Floor 4', command = lambda *args : self.make_grid(rooms4))
		floor_4.grid()
		floor_4.config(height = '2', width = '15')

		floor_5 = Button(button_frame, text = 'Floor 5', command = lambda *args : self.make_grid(rooms5))
		floor_5.grid(row = 0, column = 1)
		floor_5.config(height = '2', width = '15')

		username_label = Label(button_frame, text = 'username: ')
		username_label.grid(row = 1, column = 0)

		self.username_entry = Entry(button_frame)
		self.username_entry.grid(row = 1, column = 1)

		password_label = Label(button_frame, text = 'password: ')
		password_label.grid(row = 2, column = 0)

		self.password_entry = Entry(button_frame)
		self.password_entry.grid(row = 2, column = 1)

		self.grid_frame = Frame(self.root)
		self.grid_frame.grid(row = 3, column = 0)

		self.make_grid(rooms4)


		self.root.mainloop()

	def submit(self):

		if self.username_entry.get() == '' or self.password_entry.get() == '':
			tkinter.messagebox.showinfo('Error', 'You need to provide your Calnet username and password before you submit!')

		elif not self.room:
			tkinter.messagebox.showinfo('Error', 'You must have selected at least one time slot to proceed!')

		else:
			self.username = self.username_entry.get()
			self.password = self.password_entry.get()

			tkinter.messagebox.showinfo('Done', 'Thank you! Once the bot is finished check your email to confirm your bookings')
			self.ready = True
			self.root.destroy()

			


	def check_time_order(self, button):
		first_time = self.times_list[0]
		new_time = self.button_dict[button][1]
		last = self.times[0]
		for t in self.times[1:]:
			if t == first_time and last == new_time:
				return False
			elif t == new_time and last == first_time:
				return False
			last = t
		return True


	def get_button_values(self, event):
		button = event.widget
		if button['bg'] == 'green':

			if len(self.times_list) > 1:
				tkinter.messagebox.showinfo('Error', 'Sorry! Can only book two rooms per day.')

			elif self.room and (self.button_dict[button][0] != self.room):
				tkinter.messagebox.showinfo('Error', 'Sorry! The time slots must be in consecutive order.')

			elif len(self.times_list) > 0 and self.check_time_order(button):
				tkinter.messagebox.showinfo('Error', 'Sorry! The time slots must be in consecutive order.')

			else:
				self.room = self.button_dict[button][0] 
				self.times_list.append(self.button_dict[button][1])
				button.configure(bg = 'yellow')

		else:
			self.times_list.remove(self.button_dict[button][1])
			if len(self.times_list) == 0:
				self.room = None
			button.configure(bg = 'green')



	def make_timebuttons(self, room_dict):
		the_row = 4
		for key in room_dict:
			the_column = 1
			for t in self.times:
				time_button = Button(self.grid_frame, bg = 'green')
				time_button.grid(row = the_row, column = the_column)
				time_button.config(width = 5)
				time_button.bind('<ButtonRelease-1>', self.get_button_values)
				self.button_dict[time_button] = [key, t]
				the_column += 1
			the_row += 1


	def update_frame(self):
		self.room = None
		self.times_list = []
		self.grid_frame.destroy()
		self.grid_frame = Frame(self.root)
		self.grid_frame.grid(row = 3, column = 0)	

	def make_grid(self, room_dict):
		self.update_frame()

		if len(room_dict) == 5:
			self.floor = 4
		else:
			self.floor = 5

		place_holder = Label(self.grid_frame)
		place_holder.grid(row = 3, column = 0)

		the_row = 4
		for key in room_dict:
			label = Label(self.grid_frame, text = key+' '+room_dict[key])
			label.grid(row = the_row, column = 0)
			label.config(height = 2)
			the_row += 1

		the_column = 1
		for t in self.times:
			label = Label(self.grid_frame, text = t)
			label.grid(row = 3, column = the_column)
			label.config(width = 6)
			the_column += 1

		self.make_timebuttons(room_dict)

		submit_frame = Frame(self.root)
		submit_frame.grid(row = 12, column = 0)

		submit_button = Button(submit_frame, text = 'SUBMIT', command = self.submit)
		submit_button.grid(row = 12, column = 5)
		submit_button.configure(height = 2, width = 12)

		