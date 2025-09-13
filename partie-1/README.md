THere is repeated code in the controllers which can be refactored into a base class, however it would introduce more cognitive complexity so duplicating the code should be fine

Since tables already exist in the database, we could also use reflection to get the schemas dynamically, but in a production setting defining models with data types and constraints is preferrable.


Get note by id example, handle not foud error in the controller

transparencyemail
