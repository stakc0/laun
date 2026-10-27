function plan(name, symbol) {
  name = String(name || '').trim();
  symbol = String(symbol || '').trim().toUpperCase();
  if (!name || name.length > 32) throw new Error('name must be 1-32 characters');
  if (!/^[A-Z0-9]{1,10}$/.test(symbol)) throw new Error('symbol must be 1-10 letters or numbers');
  return { name, symbol, decimals: 9, mode: 'dry-run' };
}

export default function handler(req, res) {
  if (req.method !== 'POST') return res.status(405).json({ error: 'method not allowed' });
  try { return res.status(200).json(plan(req.body?.name, req.body?.symbol)); }
  catch (error) { return res.status(400).json({ error: error.message }); }
}
