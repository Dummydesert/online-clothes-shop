@app.route('/new_user', methods=['GET', 'POST'])
def():
    form = CreateUser()
    if form.validate_on_submit():
        create_new_user(form.username.data, form.is_admin.data)
        flash("Usuário criado com sucesso.")
		return redirect(url_for('index'))
    return render_template('new_user.html', form=form)