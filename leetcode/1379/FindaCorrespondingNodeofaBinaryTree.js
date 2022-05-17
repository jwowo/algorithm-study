var getTargetCopy = function(original, cloned, target) {
    if (!cloned) return;
    if (cloned.val === target.val) {
        return cloned;
    } else {
        return getTargetCopy(original, cloned.left, target) || getTargetCopy(original, cloned.right, target);
    }
};
