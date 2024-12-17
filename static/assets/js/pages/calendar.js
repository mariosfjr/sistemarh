$( document ).ready(function() {
    
		$('#calendar').fullCalendar({
			header: {
				left: 'prev,next today',
				center: 'title',
				right: 'month,agendaWeek,agendaDay'
			},
			defaultDate: '2024-12-12',
			editable: true,
			eventLimit: true,
			events: [
				{
					title: 'Evento',
					start: '2024-12-01'
				},
				{
					title: 'Longo Evento',
					start: '2024-12-07',
					end: '2024-12-10'
				},
				{
					id: 999,
					title: 'Evento Repetido',
					start: '2024-12-09T16:00:00'
				},
				{
					id: 999,
					title: 'Evento Repetido',
					start: '2024-12-16T16:00:00'
				},
				{
					title: 'Conferencia',
					start: '2024-12-11',
					end: '2024-12-13'
				},
				{
					title: 'Reunião',
					start: '2024-12-12T10:30:00',
					end: '2024-12-12T12:30:00'
				},
				{
					title: 'Almoço',
					start: '2024-12-12T12:00:00'
				},
				{
					title: 'Reunião',
					start: '2024-12-12T14:30:00'
				},
				{
					title: 'Happy Hour',
					start: '2024-12-12T17:30:00'
				},
				{
					title: 'Jantar',
					start: '2024-12-12T20:00:00'
				},
				{
					title: 'Festa de Aniversário',
					start: '2024-12-13T07:00:00'
				},
				{
					title: 'Google',
					url: 'http://google.com/',
					start: '2024-12-28'
				}
			]
		});

});