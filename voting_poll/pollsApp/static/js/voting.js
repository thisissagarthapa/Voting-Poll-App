document.addEventListener('DOMContentLoaded', function() {
    const voteButtons = document.querySelectorAll('.vote-btn');

    voteButtons.forEach(button => {
        button.addEventListener('click', function() {
            const selectedOption = this.parentNode.querySelector('input:checked');
            if (selectedOption) {
                const voteCount = this.parentNode.querySelector('.vote-count');
                let currentVotes = parseInt(voteCount.textContent);
                currentVotes++;
                voteCount.textContent = currentVotes;
                // Simulate server-side logic to save vote
                console.log(`Voted for ${selectedOption.value}`);
            }
        });
    });
});
