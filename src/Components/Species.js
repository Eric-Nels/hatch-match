function Species({species}) {
    return(
        <div>
            <header> Search by Species of Fish</header>
            {species.map((fish)=> {
                return(
                    <div key={fish.id} className="fish-card">
                        <h2>{fish.name}</h2>
                        <img src={fish.image} />
                    </div>
                )
            })}
        </div>
    )
}

export default Species;