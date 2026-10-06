/**
 * @param {number[]} citations
 * @return {number}
 */
var hIndex = function (citations) {
    citations.sort(function (a, b) { return b - a });
    let minCitations, h = 0;
    for (let papers = 1; papers <= citations.length; papers++) {
        minCitations = citations[papers - 1];

        h = Math.min(papers, minCitations);
        if (h >= minCitations) return h;
    }

    return h;
};


console.log(hIndex([8]));
console.log(hIndex([5, 1, 1]));
console.log(hIndex([5, 4, 3]));
console.log(hIndex([5, 4, 4, 4, 3]));