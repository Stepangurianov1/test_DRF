import logo from './logo.svg';
import './App.css';
import React from "react"
import AuthorsList from './components/Author';
import axios from "axios"
import BookList from './components/Book';
import NotFound404 from './components/NotFound404';
import {BrowserRouter, Route, Routes, Link, Navigate} from "react-router-dom"
import BookAuthors from './components/BooksAuthors';
import LoginForm from './components/Auth';
import Cookies from 'universal-cookie';
import BookForm from './components/BookForm';

class App extends React.Component{
  constructor(props){
      super(props)
      this.state = { // state - состояние
           'authors': [],
           'books': [],
           'token': '',
      }
  }
  create_book(name, authors){
    // console.log(id)
    const headers = this.get_headers()
    const data = {name:name, authors:authors}
    axios.post(`http://127.0.0.1:8000/api/books/`,data, {headers}).then(response =>{ 
      this.load_data()
    }).catch(error=> {
      console.log(error)
      this.setState({books:[]})})
  }
  delete_book(id){
    console.log(id)
    const headers = this.get_headers()
    axios.delete(`http://127.0.0.1:8000/api/books/${id}`, {headers}).then(response =>{ 
      this.load_data()
    }).catch(error=> {
      console.log(error)
      this.setState({books:[]})})
  }
  logout(){

    this.set_token('')
    this.setState({'books':[], 'authors':[]})
  }

  is_auth(){
    console.log(!!this.state.token)
    return !!this.state.token

  }

  set_token(token){
    console.log(token)
    //  localStorage.setItem('token',token)
    const cookies = new Cookies()
    cookies.set('token', token)
    this.setState({'token':token}, ()=>this.load_data())
  }

  get_token_storage(){ 
    const cookie = new Cookies()
    const token = cookie.get('token')
    console.log(token)
    this.setState({'token':token}, () => this.load_data())

  }

  get_token(username, password){

    console.log(username, password)
    const data = {username:username, password:password}
    axios.post('http://127.0.0.1:8000/api-token-auth/', data).then(response => {
      this.set_token(response.data['token'])
    }).catch(error => alert('Неверный логин или пароль'))
  }

  get_headers(){
    let headers = {
      'Content-Type': 'application/json'
      }
      if (this.is_auth())
      {
      headers['Authorization'] = 'Token ' + this.state.token
      }
      return headers
      
  }

  load_data(){
    const headers = this.get_headers()
    axios.get('http://127.0.0.1:8000/api/authors/', {headers}).then(response =>{
      this.setState(
        {
          'authors':response.data
        }
      )

    }).catch(error=> console.log(error))
    axios.get('http://127.0.0.1:8000/api/books/', {headers}).then(response =>{
      this.setState(
        {
          'books':response.data
        }
      )

    }).catch(error=> console.log(error))
  }


  componentDidMount(){ //устанавливает состояние. когда подтягивается компонент заходим сюда отрабатывает когда запрашиваем данные
    this.get_token_storage()
  }

  render(){
       return(
         <div>
          <BrowserRouter>
          <nav>
          <li>
            <Link to='/'>Authors</Link>
          </li>
          <li>
            <Link to='/books'>Books</Link>
          </li>
          <li>
            {this.is_auth() ? <button onClick={()=> this.logout()}>Logout</button> : <Link to='/login'>Login</Link>}
          </li>
          </nav>
          <Routes>
            <Route exact path='/' element={<Navigate to='/authors'/>}/>
            <Route path='/authors'>
              <Route index element={<AuthorsList authors={this.state.authors}/>}/>
              <Route path=':authorId' element={<BookAuthors books={this.state.books}/>}/>
            </Route>
            <Route exact path='/books' element={<BookList books={this.state.books} delete_book={(id)=>this.delete_book(id)}/>}/>
            <Route exact path='/books/create' element={<BookForm authors={this.state.authors} create_book={(name, authors)=>this.create_book(name, authors)}/>}/>
            
            <Route exact path='/login' element={<LoginForm get_token={(username, password) => this.get_token(username, password)}/>}/>
            <Route path='*' element={<NotFound404/>}/>
          </Routes>
          </BrowserRouter>
           
         </div>
       )

  }

}
export default App;
