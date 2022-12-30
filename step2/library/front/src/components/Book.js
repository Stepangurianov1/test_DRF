import React from 'react'
const BookItem = ({book, delete_book}) => {
console.log(book.name)
return (
<tr>
<td>
{book.name}
</td>
<td>
{book.authors}
</td>

<td>
{book.id}
</td>
<td>
    <button onClick={()=>delete_book(book.id)}tupe='button'> Delete</button>
</td>
</tr>
)
}

const BookList = ({books, delete_book}) => {
    return (
    <table>
    <th>
    Name
    </th>
    <th>
    Authors
    </th>
    <th>
    ID
    </th>
    {books.map((book_) => <BookItem book={book_} delete_book={delete_book} />)}
    </table>
    )
    }
    export default BookList
    