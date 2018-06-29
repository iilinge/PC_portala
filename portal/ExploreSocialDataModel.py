

Class CreateDataModel()


    def createNodes(self):
            try:
            Male(name='Bradley', surname='Green', age=24, country='US').save()
            Male(name='Matthew', surname='Cooper', age=36, country='US').save()
            Male(name='lohn', surname='Goodman', age=24, country='Mexico').save()
            Male(name='Ripley', surname = 'Aniston', age=89, country = 'US').save()

            # Creating FeMales

            Female(name='Lisa', surname = 'Adams', age = 15, country='Russland').save()
            Female(name='Lisa', surname='Renata', age=55, country='Russland').save()
            Female(name='Lisa', surname='Paola', age=24, country='Brazil').save()
            Female(name='Lisa', surname='Sun Ho', age=15, country='China').save()

            # Creating Movies

            Movie(movieName='Last chance').save()
            Movie(movieName='The paradise').save()
            Movie(movieName='Matrix').save()

            except UniqueProperty:

            already exists.
                Pass



