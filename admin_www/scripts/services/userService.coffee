app.factory 'userService', [
	'$rootScope', 
	'Restangular', 
	'$http', 
	'$q', 
	'localStorageService'
	, ($rootScope, Restangular, $http, $q, localStorageService) ->

		fac = {}

		user = null
		session = null

		rest = () =>
			if not session
				throw 'No user logged in, cannot get rest().'
			return Restangular.one('users', session.user_id)

		is_signed_in = () ->
			if session 
				return true
			return false

		is_guest = () ->
			if is_signed_in() and user and user.is_guest
				return true
			return false

		get_session = () ->
			return session

		set_session = (new_session) ->
			session = new_session

		get_user = () ->
			return user

		set_user = (new_user) ->
			user = new_user

		create_guest_user = (guest_token) =>
			deferred = $q.defer()
			kwargs = {
				'guest_token': guest_token
			}
			promise = Restangular.all('users').post(kwargs)
			promise.then (data) =>
				set_session(data.session)
				set_user(data.user)
				configure_http()
				persist_to_cookie()
				deferred.resolve data
			, (error) =>
				deferred.reject error
			return deferred.promise

		create_normal_user = (email_address, password, first_name, guest_token) =>
			deferred = $q.defer()
			kwargs = {
				'email_address': email_address,
				'password': password,
				'first_name': first_name,
				'guest_token': guest_token,
			}
			promise = Restangular.all('users').post(kwargs)
			promise.then (data) =>
				set_session(data.session)
				set_user(data.user)
				configure_http()
				persist_to_cookie()
				deferred.resolve data
			, (error) => 
				deferred.reject error
			return deferred.promise

		signin = (email_address, password) =>
			deferred = $q.defer()
			kwargs = {
				'email_address': email_address,
				'password': password,
			}
			promise = Restangular.all('sessions').post(kwargs)
			promise.then (data) =>
				set_session(data.session)
				set_user(data.user)
				configure_http()
				persist_to_cookie()
				deferred.resolve data
			, (error) =>
				deferred.reject error
			return deferred.promise

		signout = () =>
			deferred = $q.defer()
			promise = Restangular.one('sessions', session.id).remove()
			promise.then (data) =>
				deferred.resolve data
			, (error) =>
				deferred.reject error
			promise.finally (data) ->
				set_session(null)
				set_user(null)
				persist_to_cookie()
			return deferred.promise

		get = () =>
			deferred = $q.defer()
			rest().get().then (data) =>
				user = data.user
				deferred.resolve data
			, (error) =>
				deferred.reject error
			return deferred.promise

		persist_to_cookie = () =>
			localStorageService.set('session', session)

		load_session_from_cookie = () =>
			stored_session = localStorageService.get('session')
			if stored_session
				set_session(stored_session)
				configure_http()
				console.log 'Current session token: ' + session.token
			else
				console.log 'Not loading from cookie.'

		configure_http = () =>
			$http.defaults.headers.common.Authorization = 'xBasic ' + btoa('api:' + session.token)

		fac.get_user = get_user
		fac.get_session = get_session

		fac.load_session_from_cookie = load_session_from_cookie
		fac.is_signed_in = is_signed_in
		fac.is_guest = is_guest
		fac.get = get
		fac.signout = signout
		fac.signin = signin
		fac.create_normal_user = create_normal_user
		fac.create_guest_user = create_guest_user
		fac.user = user
		fac.session = session
		fac.rest = rest
		return fac
]
