const test = (value, depth = 0, seen = new WeakSet()) => {
  const padding = "  ".repeat(depth);
  if (seen.has(value)) {
    return '"<circular>"';
  }

  if (value === null) {
    return `${padding}null`;
  }

  switch (typeof value) {
    case "number":
      return value.toString();
    case "string":
      return `"${value}"`;
    case "object":
      seen.add(value);
      if (Array.isArray(value)) {
        const contents = value
          .map((v) => `${padding}  ${test(v, depth + 1, seen)}`)
          .join(",\n");
        seen.delete(value);
        return `[\n${contents}\n${padding}]`;
      } else {
        const contents = Object.entries(value)
          .map(([key, value]) => {
            const innerContents = test(value, depth + 1, seen);
            return `${padding}  "${key}": ${innerContents}`;
          })
          .join(",\n");
        seen.delete(value);
        return `{\n${contents}\n${padding}}`;
      }
  }
};
const a = {foo: 1}
const b = { foo: a, bar: a }

console.log(test(b));
