class Solution {
    /**
     * @param {number[]} nums1
     * @param {number[]} nums2
     * @return {number}
     */
    findMedianSortedArrays(nums1, nums2) {
        let m = this.findMedianInArr1(nums1, nums2)
        if (m === undefined) m = this.findMedianInArr1(nums1, nums2, false);
        if (m === undefined) m = this.findMedianInArr1(nums2, nums1);
        if (m === undefined) m = this.findMedianInArr1(nums2, nums1, false);
        return m;
    }

    findMedianInArr1(a1, a2, inclusive = true) {
        let l = 0, r = a1.length;
        const medianIndex = Math.floor((a1.length + a2.length - 1) / 2);

        while (l < r) {
            const m = l + Math.floor((r - l) / 2);
            const candidate = a1[m];

            let l2 = 0, r2 = a2.length;

            while (l2 < r2) {
                const m2 = l2 + Math.floor((r2 - l2) / 2);

                if (a2[m2] > candidate || (inclusive && a2[m2] === candidate)) {
                    r2 = m2;
                } else {
                    l2 = m2 + 1;
                }
            }

            if (m + l2 === medianIndex) {
                if ((a1.length + a2.length) % 2 === 0) {
                    const upperMedian = Math.min(m + 1 >= a1.length ? Infinity : a1[m + 1], l2 >= a2.length ? Infinity : a2[l2]);
                    return (candidate + upperMedian) / 2;
                }
                return candidate;
            } else if (m + l2 > medianIndex) {
                r = m;
            } else {
                l = m + 1;
            }
        }

        return undefined;
    }
}

const s = new Solution();
console.log(s.findMedianSortedArrays([], [2, 3]));
console.log(s.findMedianSortedArrays([0, 0], [0, 0]));
console.log(s.findMedianSortedArrays([1, 2], [3]));
console.log(s.findMedianSortedArrays([1, 2, 3, 4], [3, 4, 6]));
console.log(s.findMedianSortedArrays([1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 6]));
console.log(s.findMedianSortedArrays([1, 2, 3, 4], [3, 6]));
console.log(s.findMedianSortedArrays([1, 2], [3, 4]));
