db.clientes.insertOne(
	{
		nombre:"Albert",
		apellidos:"Beltran Carbonell",
		correos:[
			{	
				tipo:'personal',
				correo:'info@albert.com'
			},{	
				tipo:'trabajo',
				correo:'albert@correo.com'
			}]
	}
)
